from functional_pipeline import String, pipeline
from functools import partial


def current_excitation_setting(ctx):
    print('Set coil excitation')

    oModule         = ctx["ansys_object"]["oDesign"].GetModule("BoundarySetup")
    coil_name_list  = ctx["data"]["coil_name_list"]
    excitation_name = ctx["params"]["name_params"]["excitation"]

    N, I_ph_A, I_ph_B, I_ph_C = excitation_name["conductor_number"], excitation_name["phase_I_A"], excitation_name["phase_I_B"], excitation_name["phase_I_C"]

    def Add_winding_group(winding_name, phase_current):
        return oModule.AssignWindingGroup(
            [
                "NAME:" + winding_name,
                "Type:="		, "Current",
                "IsSolid:="		, False,
                "Current:="		, phase_current,
                "Resistance:="		, "0ohm",
                "Inductance:="		, "0nH",
                "Voltage:="		, "0mV",
                "ParallelBranchesNum:="	, "1"
            ])

    def assign_coil_group(polarity, coil_group):
        oModule.AssignCoilGroup(coil_group,
                                [
                                    "NAME:" + coil_group[0],
                                    "Objects:="		, coil_group,
                                    "Conductor number:="	, N,
                                    "PolarityType:="	, polarity
                                ])

    def add_coil_to_winding(winding, polarity, coil_group):
        def boundary_list(winding, polarity, coil):
            return [
                "NAME:" + coil,
                "Objects:="		, [coil],
                "ParentBndID:="		, winding,
                "Conductor number:="	, N,
                "Winding:="		, winding,
                "PolarityType:="	, polarity
            ]

        boundary_polarity_winding = partial(boundary_list, winding, polarity)

        oModule.AddCoilstoWinding(
            [
                "NAME:AddTerminalsToWinding",
                ["NAME:BoundaryList"] +
                list(map(boundary_polarity_winding, coil_group))
            ])

###
    # variable
    winding_group = ["Winding_A", "Winding_B", "Winding_C", ]
    current_ph_group = [I_ph_A, I_ph_B, I_ph_C]

    winding_coil_polarity_group = [
        ["Winding_A", "Negative", "Ain"],
        ["Winding_A", "Positive", "Aout"],
        ["Winding_B", "Negative", "Bin"],
        ["Winding_B", "Positive", "Bout"],
        ["Winding_C", "Negative", "Cin"],
        ["Winding_C", "Positive", "Cout"]
    ]

    # setting winding_A, B, C
    list(map(Add_winding_group, winding_group, current_ph_group))

    for winding, polarity, coil in winding_coil_polarity_group:
        # settting assign_coil_group
        pipeline(
            coil_name_list,
            [
                (filter, String.startswith(coil)),
                list,
                partial(assign_coil_group, polarity),
            ]
        )

    # settting add_coil_to_winding
        pipeline(
            coil_name_list,
            [
                (filter, String.startswith(coil)),
                list,
                partial(add_coil_to_winding, winding, polarity)
            ]
        )

    return ctx

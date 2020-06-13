# coils
import re
from functools import reduce, partial
from functional_pipeline import String, pipeline


def coils_model(ctx):
    print('Draw coil model')

    oEditor     = ctx["ansys_object"]["oEditor"]
    stator_slot = int(ctx["params"]["stator_params"]["slot"])

    oEditor.CreateUserDefinedPart(
        [
            "NAME:UserDefinedPrimitiveParameters",
            "DllName:="		, "RMxprt/LapCoil.dll",
            "Version:="		, "16.0",
            "NoOfParameters:="	, 22,
            "Library:="		, "syslib",
            [
                "NAME:ParamVector",
                [
                    "NAME:Pair",
                    "Name:="		, "DiaGap",
                    "Value:="		, "Dsi"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "DiaYoke",
                    "Value:="		, "Dso"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Length",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Skew",
                    "Value:="		, "0deg"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Slots",
                    "Value:="		, "slot"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "SlotType",
                    "Value:="		, "3"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs0",
                    "Value:="		, "Hs0"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs1",
                    "Value:="		, "Hs1"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs2",
                    "Value:="		, "Hs2"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bs0",
                    "Value:="		, "Bs0"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bs1",
                    "Value:="		, "Bs1"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bs2",
                    "Value:="		, "Bs2"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Rs",
                    "Value:="		, "Rs"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "FilletType",
                    "Value:="		, "2"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Layers",
                    "Value:="		, "2"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "CoilPitch",
                    "Value:="		, "1"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "EndExt",
                    "Value:="		, "5mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "SpanExt",
                    "Value:="		, "25mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "BendAngle",
                    "Value:="		, "0deg"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "SegAngle",
                    "Value:="		, "10deg"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "LenRegion",
                    "Value:="		, "200mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "InfoCoil",
                    "Value:="		, "1"
                ]
            ]
        ],
        [
            "NAME:Attributes",
            "Name:="		, "Coil1",
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, ctx["params"]["motor_cal_params"]["material"]["coil"],
            "SolveInside:="		, True
        ])

    def coil_muti():
        oEditor.SeparateBody(
            [
                "NAME:Selections",
                "Selections:="		, "Coil1",
                "NewPartsModelFlag:="	, "Model"
            ])
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "Coil1_Separate1"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Name",
                            "Value:="		, "Coil2"
                        ]
                    ]
                ]
            ])
        oEditor.DuplicateAroundAxis(
            [
                "NAME:Selections",
                "Selections:="		, "Coil1,Coil2",
                "NewPartsModelFlag:="	, "Model"
            ],
            [
                "NAME:DuplicateAroundAxisParameters",
                "CreateNewObjects:="	, True,
                "WhichAxis:="		, "Z",
                "AngleStr:="		, str(360/stator_slot) + "deg",
                "NumClones:="		, str(stator_slot)
            ],
            [
                "NAME:Options",
                "DuplicateAssignments:=", False
            ])
        # coil1, coil2, coil1_1, coil2_1

    def coil_nameing_and_color_for_abc_winding():
        def ansoft_coil_name_listing():
            # ['Coil1', 'Coil2', 'Coil1_1', 'Coil2_1', 'Coil1_2', 'Coil2_2', 'Coil1_3', 'Coil2_3', 'Coil1_4', 'Coil2_4', 'Coil1_5', 'Coil2_5', 'Coil1_6', 'Coil2_6', 'Coil1_7', 'Coil2_7', 'Coil1_8', 'Coil2_8', 'Coil1_9', 'Coil2_9', 'Coil1_10', 'Coil2_10', 'Coil1_11', 'Coil2_11', 'Coil1_12', 'Coil2_12', 'Coil1_13', 'Coil2_13', 'Coil1_14', 'Coil2_14', 'Coil1_15', 'Coil2_15', 'Coil1_16', 'Coil2_16', 'Coil1_17', 'Coil2_17']
            return list(
                reduce(
                    lambda total, coil_no:
                    total + ["Coil1_" + str(coil_no+1)] +
                    ["Coil2_" + str(coil_no+1)],
                    list(range(stator_slot-1)),
                    ["Coil1", "Coil2"]
                )
            )

        def expect_coil_name_listing():
            def coil_dirc_single_phase_single_side():
                # 12s10p
                #[['in', 'out'], ['out', 'in']]
                return list(
                    map(
                        lambda coil_no:
                        ["in", "out"] if coil_no % 2 == 0 else ["out", "in"],
                        list(
                            range(
                                int(stator_slot/3/2)
                            )
                        )
                    )
                )

                # 18s20p
                # return list(map(lambda coil_no: ["out", "in"] if coil_no % 2 == 0 else ["in", "out"], list(range(int(stator_slot/3/2)))))
                ##[['out', 'in'], ['in', 'out'], ['out', 'in']]

            def abc_coil_listing(coil_list, A_coil_list=[], B_coil_list=[], C_coil_list=[]):
                for idx, coil_list in enumerate(coil_list):
                    dirc_1, dirc_2 = coil_list
                    idx += 1

                    # 12s10p
                    A_coil_list.append("A" + dirc_1 + str(idx))
                    A_coil_list.append("A" + dirc_2 + str(idx))

                    B_coil_list.append("B" + dirc_2 + str(idx))
                    B_coil_list.append("B" + dirc_1 + str(idx))

                    C_coil_list.append("C" + dirc_1 + str(idx))
                    C_coil_list.append("C" + dirc_2 + str(idx))

                    # 18s20p
                    # A_coil_list.append("A"+ coil[0] + str(idx))
                    # A_coil_list.append("A"+ coil[1] + str(idx))

                    # B_coil_list.append("B"+ coil[0] + str(idx))
                    # B_coil_list.append("B"+ coil[1] + str(idx))

                    # C_coil_list.append("C"+ coil[0] + str(idx))
                    # C_coil_list.append("C"+ coil[1] + str(idx))

                return A_coil_list + B_coil_list + C_coil_list

            def abc_coil_listing_2(stator_slot, coil_list, A_coil_list=[], B_coil_list=[], C_coil_list=[]):
                for idx, coil_list in enumerate(coil_list):
                    dirc_1, dirc_2 = coil_list
                    second_side_no = idx + int(stator_slot/3/2) + 1

                    # 12s10p
                    A_coil_list.append("A" + dirc_2 + str(second_side_no))
                    A_coil_list.append("A" + dirc_1 + str(second_side_no))

                    B_coil_list.append("B" + dirc_1 + str(second_side_no))
                    B_coil_list.append("B" + dirc_2 + str(second_side_no))

                    C_coil_list.append("C" + dirc_2 + str(second_side_no))
                    C_coil_list.append("C" + dirc_1 + str(second_side_no))

                    # 18s20p
                    # A_coil_list.append("A"+ coil[0] + str(second_side_no))
                    # A_coil_list.append("A"+ coil[1] + str(second_side_no))

                    # B_coil_list.append("B"+ coil[0] + str(second_side_no))
                    # B_coil_list.append("B"+ coil[1] + str(second_side_no))

                    # C_coil_list.append("C"+ coil[0] + str(second_side_no))
                    # C_coil_list.append("C"+ coil[1] + str(second_side_no))

                return A_coil_list + B_coil_list + C_coil_list

            coil_dirc_single_phase_single_side_list = coil_dirc_single_phase_single_side()

            total_coil_list = abc_coil_listing(
                coil_dirc_single_phase_single_side_list
            )

            if int(stator_slot/3/2) > 1:
                total_coil_list_2 = abc_coil_listing_2(
                    stator_slot, coil_dirc_single_phase_single_side_list)

            return total_coil_list + total_coil_list_2
            # 12s10p
            # ['Ain1', 'Aout1', 'Aout2', 'Ain2', 'Bout1', 'Bin1', 'Bin2', 'Bout2', 'Cin1', 'Cout1', 'Cout2', 'Cin2']
            # 18s20p
            # ['Aout1', 'Ain1', 'Ain2', 'Aout2', 'Aout3', 'Ain3', 'Bout1', 'Bin1', 'Bin2', 'Bout2', 'Bout3', 'Bin3', 'Cout1', 'Cin1', 'Cin2', 'Cout2', 'Cout3', 'Cin3', 'Aout4', 'Ain4', 'Ain5', 'Aout5', 'Aout6', 'Ain6', 'Bout4', 'Bin4', 'Bin5', 'Bout5', 'Bout6', 'Bin6', 'Cout4', 'Cin4', 'Cin5', 'Cout5', 'Cout6', 'Cin6']

        def coil_naming(total_ansoft_coil, total_expect_coil):
            for ansoft_coil, expect_coil in zip(total_ansoft_coil, total_expect_coil):
                    # coil1 -> Aout1, Coil2 -> Ain1
                # coil1_1 -> Ain2, Coil2_1 -> Aout2
                # coil1_2 -> Aout3, Coil2_2 -> Ain3
                oEditor.ChangeProperty(
                    [
                        "NAME:AllTabs",
                        [
                            "NAME:Geometry3DAttributeTab",
                            [
                                "NAME:PropServers",
                                ansoft_coil
                            ],
                            [
                                "NAME:ChangedProps",
                                [
                                    "NAME:Name",
                                    "Value:="		, expect_coil
                                ]
                            ]
                        ]
                    ])

        # color setting begin
        def coil_color_setting(total_expect_coil):
            coil_color_list = [
                ["Ain",  ["NAME:Color", "R:=", 255, "G:=", 0, "B:=", 0]],
                ["Aout", ["NAME:Color", "R:=", 255, "G:=", 0, "B:=", 128]],
                ["Bin",  ["NAME:Color", "R:=", 0, "G:=", 0, "B:=", 255]],
                ["Bout", ["NAME:Color", "R:=", 0, "G:=", 128, "B:=", 255]],
                ["Cin",  ["NAME:Color", "R:=", 0, "G:=", 128, "B:=", 0]],
                ["Cout", ["NAME:Color", "R:=", 0, "G:=", 64, "B:=", 64]]
            ]

            def set_color(coil_name):
                oEditor.ChangeProperty(
                    [
                        "NAME:AllTabs",
                        [
                            "NAME:Geometry3DAttributeTab",
                            [
                                "NAME:PropServers",
                                coil_name
                            ],
                            [
                                "NAME:ChangedProps",
                                color_no
                            ]
                        ]
                    ])

            for coil_name, color_no in coil_color_list:
                pipeline(
                    total_expect_coil,
                    [
                        (filter, String.startswith(coil_name)),
                        list,
                        (map, set_color),
                        list
                    ]
                )

        # coil_nameing_and_color_for_abc_winding exec
        total_ansoft_coil = ansoft_coil_name_listing()
        total_expect_coil = expect_coil_name_listing()
        coil_naming(total_ansoft_coil, total_expect_coil)
        coil_color_setting(total_expect_coil)
        return total_expect_coil

    # function exec
    coil_muti()
    ctx["data"]["coil_name_list"] = coil_nameing_and_color_for_abc_winding()

    return ctx

# color setting end

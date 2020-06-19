# Stator

def stator_model(ctx):
    print('Draw Stator model')

    stator_params = ctx["params"]["stator_params"]
    model_name = ctx["params"]["name_params"]["stator"]

    ctx["ansys_object"]["oEditor"].CreateUserDefinedPart(
        [
            "NAME:UserDefinedPrimitiveParameters",
            "DllName:="		, "RMxprt/SlotCore.dll",
            "Version:="		, "12.1",
            "NoOfParameters:="	, 19,
            "Library:="		, "syslib",
            [
                "NAME:ParamVector",
                [
                    "NAME:Pair",
                    "Name:="		, "DiaGap",
                    "Value:="		, stator_params["Dsi"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "DiaYoke",
                    "Value:="		, stator_params["Dso"]
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
                    "Value:="		, stator_params["slot"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "SlotType",
                    "Value:="		, "3"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs0",
                    "Value:="		, stator_params["Hs0"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs01",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs1",
                    "Value:="		, stator_params["Hs1"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Hs2",
                    "Value:="		, stator_params["Hs2"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bs0",
                    "Value:="		, stator_params["Bs0"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bs1",
                    "Value:="		, stator_params["Bs1"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bs2",
                    "Value:="		, stator_params["Bs2"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Rs",
                    "Value:="		, stator_params["Rs"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "FilletType",
                    "Value:="		, "2"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "HalfSlot",
                    "Value:="		, "0"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "SegAngle",
                    "Value:="		, "15deg"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "LenRegion",
                    "Value:="		, "200mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "InfoCore",
                    "Value:="		, "0"
                ]
            ]
        ],
        [
            "NAME:Attributes",
            "Name:="		, model_name,
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, ctx["params"]["motor_cal_params"]["material"]["stator"],
            "SolveInside:="		, True
        ])

    return ctx

# Stator

def stator_model(oEditor, stator_params):
    print('Draw Stator model')

    oEditor.CreateUserDefinedPart(
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
            "Name:="		, "stator",
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"35CS250_20190702\"",
            "SolveInside:="		, True
        ])

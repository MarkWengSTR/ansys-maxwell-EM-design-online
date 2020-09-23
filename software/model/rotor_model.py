# rotor

def rotor_model(ctx):
    print('Draw rotor model')

    model_name = ctx["params"]["name_params"]["rotor"]

    ctx["ansys_object"]["oEditor"].CreateUserDefinedPart(
        [
            "NAME:UserDefinedPrimitiveParameters",
            "DllName:="		, "RMxprt/PMCore.dll",
            "Version:="		, "12.0",
            "NoOfParameters:="	, 13,
            "Library:="		, "syslib",
            [
                "NAME:ParamVector",
                [
                    "NAME:Pair",
                    "Name:="		, "DiaGap",
                    "Value:="		, "Dro"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "DiaYoke",
                    "Value:="		, "Dri"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Length",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Poles",
                    "Value:="		, "pole"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "PoleType",
                    "Value:="		, "rotor_type"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Embrace",
                    "Value:="		, "mag_emb"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "ThickMag",
                    "Value:="		, "mag_thick"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "WidthMag",
                    "Value:="		, "mag_width"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Offset",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bridge",
                    "Value:="		, "rotor_bridge"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Rib",
                    "Value:="		, "rotor_rib"
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
            "MaterialValue:="	, ctx["params"]["motor_cal_params"]["material"]["rotor"],
            "SolveInside:="		, True
        ])

    return ctx

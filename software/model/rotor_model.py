# rotor

def rotor_model(ctx):
    print('Draw rotor model')

    rotor_params = ctx["params"]["rotor_params"]
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
                    "Value:="		, rotor_params["Dro"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "DiaYoke",
                    "Value:="		, rotor_params["Dri"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Length",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Poles",
                    "Value:="		, rotor_params["pole"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "PoleType",
                    "Value:="		, rotor_params["rotor_type"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Embrace",
                    "Value:="		, rotor_params["mag_emb"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "ThickMag",
                    "Value:="		, rotor_params["mag_thick"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "WidthMag",
                    "Value:="		, rotor_params["mag_width"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Offset",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bridge",
                    "Value:="		, rotor_params["rotor_bridge"]
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Rib",
                    "Value:="		, rotor_params["rotor_rib"]
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

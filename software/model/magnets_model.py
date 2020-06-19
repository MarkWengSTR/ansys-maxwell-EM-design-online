# magmets


def magnets_model(ctx):
    print('Draw magnet model and set vector')

    rotor_params = ctx["params"]["rotor_params"]
    rotor_pole = int(rotor_params["pole"])
    oEditor = ctx["ansys_object"]["oEditor"]

    oEditor.CreateUserDefinedPart(
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
                    "Value:="		, "2"
                ]
            ]
        ],
        [
            "NAME:Attributes",
            "Name:="		, "magnet",
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, ctx["params"]["motor_cal_params"]["material"]["magnet"],
            "SolveInside:="		, True
        ])

    def muti_mag():
        oEditor.DuplicateAroundAxis(
            [
                "NAME:Selections",
                "Selections:="		, "magnet",
                "NewPartsModelFlag:="	, "Model"
            ],
            [
                "NAME:DuplicateAroundAxisParameters",
                "CreateNewObjects:="	, True,
                "WhichAxis:="		, "Z",
                "AngleStr:="		, str(360/rotor_pole) + "deg",
                "NumClones:="		, str(rotor_pole)
            ],
            [
                "NAME:Options",
                "DuplicateAssignments:=", False
            ])

        return True

    def vector_set(pole_num, mag_arrange_angle, direction):
        psi_direction = {
            "N": "0deg",
            "S": "180deg"
        }
        oEditor.SetWCS(
            [
                "NAME:SetWCS Parameter",
                "Working Coordinate System:=", "Global",
                "RegionDepCSOk:="	, False
            ])
        oEditor.CreateRelativeCS(
            [
                "NAME:RelativeCSParameters",
                "Mode:="		, "Axis/Position",
                "OriginX:="		, "0mm",
                "OriginY:="		, "0mm",
                "OriginZ:="		, "0mm",
                "XAxisXvec:="		, "21mm",
                "XAxisYvec:="		, "0mm",
                "XAxisZvec:="		, "0mm",
                "YAxisXvec:="		, "-0mm",
                "YAxisYvec:="		, "21mm",
                "YAxisZvec:="		, "0mm"
            ],
            [
                "NAME:Attributes",
                "Name:="		, "RelativeCS" + str(pole_num)
            ])
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DCSTab",
                    [
                        "NAME:PropServers",
                        "RelativeCS" + str(pole_num)
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Mode",
                            "Value:="		, "Euler Angle ZXZ"
                        ]
                    ]
                ]
            ])
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DCSTab",
                    [
                        "NAME:PropServers",
                        "RelativeCS" + str(pole_num)
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Psi",
                            "Value:="		, psi_direction[direction]
                        ]
                    ]
                ]
            ])
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DCSTab",
                    [
                        "NAME:PropServers",
                        "RelativeCS" + str(pole_num)
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Phi",
                            "Value:="		, str(mag_arrange_angle) + "deg"
                        ]
                    ]
                ]
            ])
        oEditor.SetWCS(
            [
                "NAME:SetWCS Parameter",
                "Working Coordinate System:=", "Global",
                "RegionDepCSOk:="	, False
            ])

    def set_vector_to_mag(pole_num):
        # magnet number: magnet, magner_1, magnet_2 ...
        number_in_name = "" if pole_num == 0 else "_" + str(pole_num)

        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "magnet" + number_in_name
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Orientation",
                            "Value:="		, "RelativeCS" + str(pole_num)
                        ]
                    ]
                ]
            ])

    def set_mag_color(pole_num, direction):
        number_in_name = "" if pole_num == 0 else "_" + str(pole_num)

        coil_color_dir = {
            "N":  ["NAME:Color", "R:=", 255, "G:=", 0, "B:=", 0],
            "S":  ["NAME:Color", "R:=", 0, "G:=", 0, "B:=", 255],
        }

        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "magnet" + number_in_name
                    ],
                    [
                        "NAME:ChangedProps",
                        coil_color_dir[direction]
                    ]
                ]
            ])

    def prepare_mag_name_list(ctx):
        for pole_num in list(range(rotor_pole)):
            number_in_name = "" if pole_num == 0 else "_" + str(pole_num)

            ctx["data"]["mag_name_list"] += ["magnet" + number_in_name]

        return ctx


    def set_color_vector_to_each_magnet():
        # magnet_number is 0..rotor_pole-1
        ini_angle = (360 / rotor_pole / 2)
        angle = (360 / rotor_pole)

        pole_no_list = list(range(rotor_pole))
        angle_list = list(map(
            lambda p_no: (ini_angle + p_no*angle),
            pole_no_list))
        direction_list = list(map(
            lambda p_no: ("S" if (p_no % 2 == 1) else "N"),
            pole_no_list))

        list(map(vector_set, pole_no_list, angle_list, direction_list))
        list(map(set_vector_to_mag, pole_no_list))
        list(map(set_mag_color, pole_no_list, direction_list))

        return True


    # exec function
    muti_mag() and \
        set_color_vector_to_each_magnet() and \
        prepare_mag_name_list(ctx)

    return ctx

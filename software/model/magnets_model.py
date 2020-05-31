# magmets


def magnets_model(oEditor, rotor_pole, rotor_params_name_list):
    print('Draw magnet model and set vector')

    Dro, Dri, pole, rotor_type, mag_emb, mag_thick, mag_width, rotor_bridge, rotor_rib = rotor_params_name_list

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
                    "Value:="		, Dro
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "DiaYoke",
                    "Value:="		, Dri
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Length",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Poles",
                    "Value:="		, pole
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "PoleType",
                    "Value:="		, rotor_type
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Embrace",
                    "Value:="		, mag_emb
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "ThickMag",
                    "Value:="		, mag_thick
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "WidthMag",
                    "Value:="		, mag_width
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Offset",
                    "Value:="		, "0mm"
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Bridge",
                    "Value:="		, rotor_bridge
                ],
                [
                    "NAME:Pair",
                    "Name:="		, "Rib",
                    "Value:="		, rotor_rib
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
            "MaterialValue:="	, "\"ZH_N44SH_20deg_20190702\"",
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

    def muti_vector_set():
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

        set_color_vector_to_each_magnet()

    # exec function
    muti_mag()
    muti_vector_set()

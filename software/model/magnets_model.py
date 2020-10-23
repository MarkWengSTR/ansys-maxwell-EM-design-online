# magmets

def prepare_mag_name_list(mag_ctx):
    # magnet_number is 0..rotor_pole-1
    # magnet name: magnet, magner_1, magnet_2 ...

    for pole_num in list(range(mag_ctx["rotor_pole"])):
        number_in_name = "" if pole_num == 0 else "_" + str(pole_num)

        mag_ctx["mag_name_list"] += ["magnet" + number_in_name]

    return mag_ctx


def create_ini_magnet(mag_ctx):
    oEditor = mag_ctx["oEditor"]
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
                    "Value:="		, "2"
                ]
            ]
        ],
        [
            "NAME:Attributes",
            "Name:="		, mag_ctx["ini_mag_name"],
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, mag_ctx["mag_material"],
            "SolveInside:="		, True
        ])

    return mag_ctx


def muti_mag(mag_ctx):
    oEditor = mag_ctx["oEditor"]
    oEditor.DuplicateAroundAxis(
        [
            "NAME:Selections",
            "Selections:="		, mag_ctx["ini_mag_name"],
            "NewPartsModelFlag:="	, "Model"
        ],
        [
            "NAME:DuplicateAroundAxisParameters",
            "CreateNewObjects:="	, True,
            "WhichAxis:="		, "Z",
            "AngleStr:="		, str(360/mag_ctx["rotor_pole"]) + "deg",
            "NumClones:="		, str(mag_ctx["rotor_pole"])
        ],
        [
            "NAME:Options",
            "DuplicateAssignments:=", False
        ])

    return mag_ctx


def create_vector(mag_ctx):
    oEditor = mag_ctx["oEditor"]
    pole_no_list = mag_ctx["pole_no_list"]
    angle_list = mag_ctx["angle_list"]
    direction_list = mag_ctx["direction_list"]

    for pole_num, mag_arrange_angle, direction in zip(pole_no_list, angle_list, direction_list):
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

    return mag_ctx


def set_vector_to_mag(mag_ctx):
    oEditor = mag_ctx["oEditor"]
    pole_no_list = mag_ctx["pole_no_list"]
    mag_name_list = mag_ctx["mag_name_list"]

    for pole_num, mag_name in zip(pole_no_list, mag_name_list):
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers", mag_name
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

    return mag_ctx


def set_mag_color(mag_ctx):
    oEditor = mag_ctx["oEditor"]
    direction_list = mag_ctx["direction_list"]
    mag_name_list = mag_ctx["mag_name_list"]

    for direction, mag_name in zip(direction_list, mag_name_list):
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
                        "NAME:PropServers", mag_name
                    ],
                    [
                        "NAME:ChangedProps",
                        coil_color_dir[direction]
                    ]
                ]
            ])

    return mag_ctx


def magnets_model(ctx):
    print('Draw magnet model and set vector')

    rotor_pole = int(ctx["params"]["rotor_params"]["pole"])
    ini_angle = (360 / rotor_pole / 2)
    angle = (360 / rotor_pole)
    pole_no_list = list(range(rotor_pole))
    angle_list = list(map(
        lambda p_no: (ini_angle + p_no*angle),
        pole_no_list))
    direction_list = list(map(
        lambda p_no: ("S" if (p_no % 2 == 1) else "N"),
        pole_no_list))

    mag_ctx = {
        "oEditor": ctx["ansys_object"]["oEditor"],
        "rotor_pole": rotor_pole,
        "ini_mag_name": "magnet",
        "mag_material": ctx["params"]["motor_cal_params"]["material"]["magnet"],
        "pole_no_list": pole_no_list,
        "angle_list": angle_list,
        "direction_list": direction_list,
        "mag_name_list": [],
    }

    prepare_mag_name_list(mag_ctx) and \
        create_ini_magnet(mag_ctx) and \
        muti_mag(mag_ctx) and \
        create_vector(mag_ctx) and \
        set_vector_to_mag(mag_ctx) and \
        set_mag_color(mag_ctx)

    ctx["data"]["mag_name_list"] = mag_ctx["mag_name_list"]

    return ctx

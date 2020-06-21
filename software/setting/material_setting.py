def material_setting(ctx):
    material_ctx = {
        "magnet_name": ctx["params"]["motor_cal_params"]["material"]["magnet"].replace("\"", ""),
        "steel_name": ctx["params"]["motor_cal_params"]["material"]["stator"].replace("\"", ""),
        "module": ctx["ansys_object"]["oProject"].GetDefinitionManager(),
    }

    print("material setting")
    add_magnet_setting(material_ctx) and \
        add_steel_setting(material_ctx)

    return ctx

def add_magnet_setting(material_ctx):
    if bool(material_ctx["module"].DoesMaterialExist(material_ctx["magnet_name"])):
        None
    else:
        material_ctx["module"].AddMaterial(
                [
                        "NAME:" + material_ctx["magnet_name"],
                        "CoordinateSystemType:=", "Cartesian",
                        "BulkOrSurfaceType:="	, 1,
                        [
                                "NAME:PhysicsTypes",
                                "set:="			, ["Electromagnetic"]
                        ],
                        "permeability:="	, "1.06650219597662",
                        "conductivity:="	, "625000",
                        [
                                "NAME:magnetic_coercivity",
                                "property_type:="	, "VectorProperty",
                                "Magnitude:="		, "-970kA_per_meter",
                                "DirComp1:="		, "1",
                                "DirComp2:="		, "0",
                                "DirComp3:="		, "0"
                        ]
                ])
    return material_ctx

def add_steel_setting(material_ctx):
    if bool(material_ctx["module"].DoesMaterialExist(material_ctx["steel_name"])):
        None
    else:
        material_ctx["module"].AddMaterial(
                [
                        "NAME:" + material_ctx["steel_name"],
                        "CoordinateSystemType:=", "Cartesian",
                        "BulkOrSurfaceType:="	, 1,
                        [
                                "NAME:PhysicsTypes",
                                "set:="			, ["Electromagnetic"]
                        ],
                        [
                                "NAME:AttachedData",
                                [
                                        "NAME:CoreLossMultiCurveData",
                                        "property_data:="	, "coreloss_multi_curve_data",
                                        "coreloss_unit:="	, "w_per_kg",
                                        [
                                                "NAME:AllCurves",
                                                [
                                                        "NAME:OneCurve",
                                                        "Frequency:="		, "50Hz",
                                                        [
                                                                "NAME:Coordinates",
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0,
                                                                        "Y:="			, 0
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.082126,
                                                                        "Y:="			, 0.010785
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.19661,
                                                                        "Y:="			, 0.060342
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.37832,
                                                                        "Y:="			, 0.1907
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.56633,
                                                                        "Y:="			, 0.3711
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.72816,
                                                                        "Y:="			, 0.55896
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.85457,
                                                                        "Y:="			, 0.72653
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.95124,
                                                                        "Y:="			, 0.86882
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.023,
                                                                        "Y:="			, 0.98313
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.0837,
                                                                        "Y:="			, 1.088
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.1281,
                                                                        "Y:="			, 1.1682
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.1699,
                                                                        "Y:="			, 1.2485
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.201,
                                                                        "Y:="			, 1.3116
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2274,
                                                                        "Y:="			, 1.3677
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2484,
                                                                        "Y:="			, 1.4145
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2683,
                                                                        "Y:="			, 1.4597
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2849,
                                                                        "Y:="			, 1.4994
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.299,
                                                                        "Y:="			, 1.5338
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3104,
                                                                        "Y:="			, 1.563
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3227,
                                                                        "Y:="			, 1.5944
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3414,
                                                                        "Y:="			, 1.6454
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3579,
                                                                        "Y:="			, 1.692
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3707,
                                                                        "Y:="			, 1.7289
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3826,
                                                                        "Y:="			, 1.765
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3925,
                                                                        "Y:="			, 1.7957
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4033,
                                                                        "Y:="			, 1.8297
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4128,
                                                                        "Y:="			, 1.8608
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4208,
                                                                        "Y:="			, 1.8884
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4283,
                                                                        "Y:="			, 1.9135
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4353,
                                                                        "Y:="			, 1.9381
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4413,
                                                                        "Y:="			, 1.9586
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4474,
                                                                        "Y:="			, 1.9793
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4525,
                                                                        "Y:="			, 1.9974
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4622,
                                                                        "Y:="			, 2.0317
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4706,
                                                                        "Y:="			, 2.0625
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4779,
                                                                        "Y:="			, 2.0888
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4852,
                                                                        "Y:="			, 2.1159
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.492,
                                                                        "Y:="			, 2.1413
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4978,
                                                                        "Y:="			, 2.1599
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5033,
                                                                        "Y:="			, 2.1834
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5083,
                                                                        "Y:="			, 2.2009
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5137,
                                                                        "Y:="			, 2.2206
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5186,
                                                                        "Y:="			, 2.2384
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5575,
                                                                        "Y:="			, 2.38
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5877,
                                                                        "Y:="			, 2.4856
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.6125,
                                                                        "Y:="			, 2.5645
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.6346,
                                                                        "Y:="			, 2.6324
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.6546,
                                                                        "Y:="			, 2.692
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.6724,
                                                                        "Y:="			, 2.7539
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.6896,
                                                                        "Y:="			, 2.8039
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.7049,
                                                                        "Y:="			, 2.8469
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.7335,
                                                                        "Y:="			, 2.9301
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.7591,
                                                                        "Y:="			, 3.0205
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.782,
                                                                        "Y:="			, 3.0827
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.8027,
                                                                        "Y:="			, 3.161
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.8217,
                                                                        "Y:="			, 3.2159
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.8623,
                                                                        "Y:="			, 3.325
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.8952,
                                                                        "Y:="			, 3.4333
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.9208,
                                                                        "Y:="			, 3.5014
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.941,
                                                                        "Y:="			, 3.5283
                                                                ]
                                                        ]
                                                ],
                                                [
                                                        "NAME:OneCurve",
                                                        "Frequency:="		, "400Hz",
                                                        [
                                                                "NAME:Coordinates",
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0,
                                                                        "Y:="			, 0
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.050769,
                                                                        "Y:="			, 0.068195
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.097532,
                                                                        "Y:="			, 0.25864
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.15985,
                                                                        "Y:="			, 0.67753
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.24064,
                                                                        "Y:="			, 1.4415
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.33668,
                                                                        "Y:="			, 2.6223
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.44345,
                                                                        "Y:="			, 4.2379
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.55002,
                                                                        "Y:="			, 6.1677
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.6606,
                                                                        "Y:="			, 8.5108
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.75539,
                                                                        "Y:="			, 10.812
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.84532,
                                                                        "Y:="			, 13.276
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.92469,
                                                                        "Y:="			, 15.701
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.99826,
                                                                        "Y:="			, 18.18
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.0757,
                                                                        "Y:="			, 21.072
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.1412,
                                                                        "Y:="			, 23.761
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2015,
                                                                        "Y:="			, 26.488
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.242,
                                                                        "Y:="			, 28.455
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2656,
                                                                        "Y:="			, 29.662
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2835,
                                                                        "Y:="			, 30.602
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3001,
                                                                        "Y:="			, 31.501
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.321,
                                                                        "Y:="			, 32.666
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3413,
                                                                        "Y:="			, 33.811
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.356,
                                                                        "Y:="			, 34.778
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.368,
                                                                        "Y:="			, 35.496
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3784,
                                                                        "Y:="			, 36.174
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3894,
                                                                        "Y:="			, 36.849
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3995,
                                                                        "Y:="			, 37.53
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4086,
                                                                        "Y:="			, 38.161
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4156,
                                                                        "Y:="			, 38.681
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4219,
                                                                        "Y:="			, 39.123
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4288,
                                                                        "Y:="			, 39.629
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4349,
                                                                        "Y:="			, 40.081
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4398,
                                                                        "Y:="			, 40.454
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.45,
                                                                        "Y:="			, 41.33
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4576,
                                                                        "Y:="			, 41.926
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4667,
                                                                        "Y:="			, 42.655
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4738,
                                                                        "Y:="			, 43.218
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4802,
                                                                        "Y:="			, 43.789
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4869,
                                                                        "Y:="			, 44.348
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4913,
                                                                        "Y:="			, 44.734
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.4966,
                                                                        "Y:="			, 45.213
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5023,
                                                                        "Y:="			, 45.675
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.506,
                                                                        "Y:="			, 45.977
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5144,
                                                                        "Y:="			, 46.809
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5238,
                                                                        "Y:="			, 47.672
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.5309,
                                                                        "Y:="			, 48.366
                                                                ]
                                                        ]
                                                ],
                                                [
                                                        "NAME:OneCurve",
                                                        "Frequency:="		, "1000Hz",
                                                        [
                                                                "NAME:Coordinates",
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0,
                                                                        "Y:="			, 0
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.044836,
                                                                        "Y:="			, 0.21917
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.07659,
                                                                        "Y:="			, 0.63568
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.11369,
                                                                        "Y:="			, 1.3634
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.15667,
                                                                        "Y:="			, 2.5073
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.20449,
                                                                        "Y:="			, 4.117
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.2558,
                                                                        "Y:="			, 6.2011
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.31259,
                                                                        "Y:="			, 8.9218
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.36853,
                                                                        "Y:="			, 11.959
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.43248,
                                                                        "Y:="			, 15.874
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.49395,
                                                                        "Y:="			, 20.146
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.55105,
                                                                        "Y:="			, 24.581
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.60421,
                                                                        "Y:="			, 29.169
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.65394,
                                                                        "Y:="			, 33.78
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.70065,
                                                                        "Y:="			, 38.568
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.74416,
                                                                        "Y:="			, 43.375
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.78702,
                                                                        "Y:="			, 48.464
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.82778,
                                                                        "Y:="			, 53.632
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.86668,
                                                                        "Y:="			, 58.929
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.90453,
                                                                        "Y:="			, 64.446
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 0.97607,
                                                                        "Y:="			, 75.859
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.041,
                                                                        "Y:="			, 87.334
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.1025,
                                                                        "Y:="			, 99.62
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.1585,
                                                                        "Y:="			, 111.81
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2123,
                                                                        "Y:="			, 124.55
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.2752,
                                                                        "Y:="			, 141
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.331,
                                                                        "Y:="			, 156.86
                                                                ],
                                                                [
                                                                        "NAME:Coordinate",
                                                                        "X:="			, 1.3897,
                                                                        "Y:="			, 175.18
                                                                ]
                                                        ]
                                                ]
                                        ]
                                ]
                        ],
                        [
                                "NAME:permeability",
                                "property_type:="	, "nonlinear",
                                "BType:="		, "normal",
                                "HUnit:="		, "A_per_meter",
                                "BUnit:="		, "tesla",
                                [
                                        "NAME:BHCoordinates",
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 0,
                                                "Y:="			, 0
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 20.54,
                                                "Y:="			, 0.065
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 41.15,
                                                "Y:="			, 0.238
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 60.94,
                                                "Y:="			, 0.541
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 80.68,
                                                "Y:="			, 0.755
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 100.17,
                                                "Y:="			, 0.906
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 125.56,
                                                "Y:="			, 1.04
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 150.6,
                                                "Y:="			, 1.13
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 175.18,
                                                "Y:="			, 1.194
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 200.47,
                                                "Y:="			, 1.239
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 225.57,
                                                "Y:="			, 1.274
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 250.45,
                                                "Y:="			, 1.301
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 275.26,
                                                "Y:="			, 1.322
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 300.36,
                                                "Y:="			, 1.34
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 350.42,
                                                "Y:="			, 1.367
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 400.16,
                                                "Y:="			, 1.388
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 452.15,
                                                "Y:="			, 1.405
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 506.02,
                                                "Y:="			, 1.419
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 553.74,
                                                "Y:="			, 1.43
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 600.74,
                                                "Y:="			, 1.439
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 653.35,
                                                "Y:="			, 1.448
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 704.25,
                                                "Y:="			, 1.456
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 750.62,
                                                "Y:="			, 1.463
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 802.89,
                                                "Y:="			, 1.469
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 847.4,
                                                "Y:="			, 1.474
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 902.52,
                                                "Y:="			, 1.48
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 958.28,
                                                "Y:="			, 1.486
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 1005.9,
                                                "Y:="			, 1.491
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 1502.3,
                                                "Y:="			, 1.531
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 2002.3,
                                                "Y:="			, 1.561
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 2501.4,
                                                "Y:="			, 1.586
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 3005,
                                                "Y:="			, 1.608
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 3505.1,
                                                "Y:="			, 1.628
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 4004.3,
                                                "Y:="			, 1.647
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 4502.8,
                                                "Y:="			, 1.663
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 5003.4,
                                                "Y:="			, 1.678
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 6009.6,
                                                "Y:="			, 1.709
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 7006.8,
                                                "Y:="			, 1.734
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 8010.2,
                                                "Y:="			, 1.758
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 9004.5,
                                                "Y:="			, 1.778
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 10005,
                                                "Y:="			, 1.797
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 28000,
                                                "Y:="			, 1.85
                                        ],
                                        [
                                                "NAME:Coordinate",
                                                "X:="			, 150000,
                                                "Y:="			, 2.05
                                        ]
                                ]
                        ],
                        [
                                "NAME:magnetic_coercivity",
                                "property_type:="	, "VectorProperty",
                                "Magnitude:="		, "0A_per_meter",
                                "DirComp1:="		, "1",
                                "DirComp2:="		, "0",
                                "DirComp3:="		, "0"
                        ],
                        [
                                "NAME:core_loss_type",
                                "property_type:="	, "ChoiceProperty",
                                "Choice:="		, "Electrical Steel"
                        ],
                        "core_loss_kh:="	, "182.197975942966",
                        "core_loss_kc:="	, "0.464858533103917",
                        "core_loss_ke:="	, "0",
                        "core_loss_kdc:="	, "0",
                        "mass_density:="	, "7600",
                        "core_loss_equiv_cut_depth:=", "0"
                ])
    return material_ctx

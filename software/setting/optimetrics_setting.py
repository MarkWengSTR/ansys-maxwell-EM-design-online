def optimetrics_setting(oProject, oDesign, total_params, reset='set_first_time'):
    max_power, max_speed = total_params["optiparametric_params"]["max_power"], total_params["optiparametric_params"]["max_speed"]
    opt_name = "OPT"
    oModule = oDesign.GetModule("Optimetrics")

    def opt_setting():
        oModule.InsertSetup("OptiParametric",
                            [
                                "NAME:" + opt_name,
                                "IsEnabled:="		, True,
                                [
                                    "NAME:ProdOptiSetupData",
                                    "SaveFields:="		, False,
                                    "CopyMesh:="		, False
                                ],
                                [
                                    "NAME:StartingPoint"
                                ],
                                "Sim. Setups:="		, ["setup1"],
                                [
                                        "NAME:Sweeps",
                                        [
                                                "NAME:SweepDefinition",
                                                "Variable:="		, "Im",
                                                "Data:="		, "0A",
                                                "OffsetF1:="		, False,
                                                "Synchronize:="		, 0
                                        ],
                                        [
                                                "NAME:SweepDefinition",
                                                "Variable:="		, "speed_rpm",
                                                "Data:="		, "1000rpm",
                                                "OffsetF1:="		, False,
                                                "Synchronize:="		, 0
                                        ]
                                ],
                                [
                                        "NAME:Sweep Operations",
                                        "add:=", max_power,
                                        "add:=", max_speed ,
                                ],
                                [
                                    "NAME:Goals"
                                ]
                            ])

#     def opt_re_setting(var_name, var_data):
#         oModule.EditSetup(opt_name,
#                           [
#                               "NAME:" + opt_name,
#                               "IsEnabled:="		, True,
#                               [
#                                   "NAME:ProdOptiSetupData",
#                                   "SaveFields:="		, False,
#                                   "CopyMesh:="		, False
#                               ],
#                               [
#                                   "NAME:StartingPoint"
#                               ],
#                               "Sim. Setups:="		, ["setup1"],
#                               [
#                                   "NAME:Sweeps",
#                                   [
#                                       "NAME:SweepDefinition",
#                                       "Variable:="	, var_name,
#                                       "Data:="		, var_data,
#                                       "OffsetF1:="	, False,
#                                       "Synchronize:="	, 0
#                                   ]
#                               ],
#                               [
#                                   "NAME:Sweep Operations"
#                               ],
#                               [
#                                   "NAME:Goals"
#                               ]
#                           ])

    # exec
    opt_setting()

    # if reset == 'set_first_time':
    #     list(map(opt_setting,
    #              opt_name_list, opt_data_list
    #              ))
    # else:
    #     list(map(opt_re_setting,
    #              opt_name_list, opt_data_list
    #              ))

    return oModule, opt_name

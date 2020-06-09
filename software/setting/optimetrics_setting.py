def optimetrics_setting(oProject, oDesign, total_params, reset='set_first_time'):
    variables_dict, analysis_name = total_params["optiparametric"], total_params["analysis_params"]["name"]
    opt_name = "OPT"
    oModule = oDesign.GetModule("Optimetrics")
    opt_name_list = list(variables_dict.keys())
    opt_data_list = list(variables_dict.values())

    def opt_setting(opt_params):
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
                                                "Data:="		, "1A",
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
                                        "add:=", ["20A","3000rpm"],
                                        "add:=", ["0A","3000rpm"],
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
    list(map(opt_setting,
             opt_name_list, opt_data_list
             ))

    # if reset == 'set_first_time':
    #     list(map(opt_setting,
    #              opt_name_list, opt_data_list
    #              ))
    # else:
    #     list(map(opt_re_setting,
    #              opt_name_list, opt_data_list
    #              ))

    return oModule, opt_name

def optimetrics_setting(oProject, oDesign, variables_dict, analysis_name, reset='set_first_time'):
    opt_name = "OPT"
    oModule = oDesign.GetModule("Optimetrics")
    opt_name_list = list(variables_dict.keys())
    opt_data_list = list(variables_dict.values())

    def opt_setting(var_name, var_data):
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
                                "Sim. Setups:="		, [analysis_name],
                                [
                                    "NAME:Sweeps",
                                    [
                                        "NAME:SweepDefinition",
                                        "Variable:="	, var_name,
                                        "Data:="		, var_data,
                                        "OffsetF1:="		, False,
                                        "Synchronize:="		, 0
                                    ]
                                ],
                                [
                                    "NAME:Sweep Operations"
                                ],
                                [
                                    "NAME:Goals"
                                ]
                            ])

    def opt_re_setting(var_name, var_data):
        oModule.EditSetup("OPT",
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
                              "Sim. Setups:="		, [analysis_name],
                              [
                                  "NAME:Sweeps",
                                  [
                                      "NAME:SweepDefinition",
                                      "Variable:="	, var_name,
                                      "Data:="		, var_data,
                                      "OffsetF1:="		, False,
                                      "Synchronize:="		, 0
                                  ]
                              ],
                              [
                                  "NAME:Sweep Operations"
                              ],
                              [
                                  "NAME:Goals"
                              ]
                          ])

    # exec
    if reset == 'set_first_time':
        list(map(opt_setting,
                 opt_name_list, opt_data_list
                 ))
    else:
        list(map(opt_re_setting,
                 opt_name_list, opt_data_list
                 ))

    return oModule, opt_name

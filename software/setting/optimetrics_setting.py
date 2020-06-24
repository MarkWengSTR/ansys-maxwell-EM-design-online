def optimetrics_setting(ctx):
    max_power = ctx["params"]["optiparametric_params"]["max_power"]
    max_speed = ctx["params"]["optiparametric_params"]["max_speed"]
    opt_name = ctx["data"]["opt_name"]
    opt_oModule = ctx["ansys_object"]["oDesign"].GetModule("Optimetrics")

    def opt_setting():
        opt_oModule.InsertSetup("OptiParametric",
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
                                ],
                                [
                                    "NAME:Goals"
                                ]
                            ])

#     def opt_re_setting(var_name, var_data):
#         opt_oModule.EditSetup(opt_name,
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

    ctx["data"]["opt_oModule"] = opt_oModule

    return ctx

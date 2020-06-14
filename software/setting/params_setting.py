# params setting


def params_setting(ctx):
    print('params setting')

    params = ctx["params"]

    total_setting_params = {**params["stator_params"], **params["rotor_params"],
                            **params["other_motor_params"], **params["band_params"], **params["excitation_params"]}

    for params_name, params_value in total_setting_params.items():
        ctx["ansys_object"]["oDesign"].ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:LocalVariableTab",
                    [
                        "NAME:PropServers",
                        "LocalVariables"
                    ],
                    [
                        "NAME:NewProps",
                        [
                            "NAME:" + params_name,
                            "PropType:=", "VariableProp",
                            "UserDef:=", True,
                            "Value:=", params_value
                        ]
                    ]
                ]
            ])

    return ctx

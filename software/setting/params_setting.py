# params setting

def params_setting(oDesign, total_params):
    print('params setting')

    total_setting_params = {**total_params["stator_params"], **total_params["rotor_params"],
                         **total_params["motor_params"], **total_params["band_params"], **total_params["excitation_params"]}
    # import ipdb; ipdb.set_trace()
    for params_name, params_value in total_setting_params.items():
        oDesign.ChangeProperty(
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
                            "NAME:"+ params_name,
                            "PropType:=", "VariableProp",
                            "UserDef:=", True,
                            "Value:=", params_value
                        ]
                    ]
                ]
            ])

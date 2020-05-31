# params setting

def params_setting(oDesign, total_params):
    print('params setting')

    for params_name, params_value in total_params.items():
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

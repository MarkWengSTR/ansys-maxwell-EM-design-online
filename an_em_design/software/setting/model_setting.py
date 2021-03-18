def model_setting(ctx):
    ctx["ansys_object"]["oDesign"]
    print('set model params')

    ctx["ansys_object"]["oDesign"].SetDesignSettings(
        [
            "NAME:Design Settings Data",
            "PreserveTranSolnAfterDatasetEdit:=", False,
            "ComputeTransientInductance:=", False,
            "ComputeIncrementalMatrix:=", False,
            "PerfectConductorThreshold:=", 1E+030,
            "InsulatorThreshold:="	, 1,
            "ModelDepth:="		, ctx["params"]["other_motor_params"]["length"],
            "UseSkewModel:="	, False,
            "EnableTranTranLinkWithSimplorer:=", False,
            "BackgroundMaterialName:=", "vacuum",
            "Multiplier:="		, ctx["params"]["other_motor_params"]["multiplier"]
        ])

    return ctx

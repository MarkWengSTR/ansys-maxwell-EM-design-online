def model_setting(oDesign, length, multiplier):
    print('set model params')

    oDesign.SetDesignSettings(
        [
            "NAME:Design Settings Data",
            "PreserveTranSolnAfterDatasetEdit:=", False,
            "ComputeTransientInductance:=", False,
            "ComputeIncrementalMatrix:=", False,
            "PerfectConductorThreshold:=", 1E+030,
            "InsulatorThreshold:="	, 1,
            "ModelDepth:="		, length,
            "UseSkewModel:="	, False,
            "EnableTranTranLinkWithSimplorer:=", False,
            "BackgroundMaterialName:=", "vacuum",
            "Multiplier:="		, multiplier
        ])

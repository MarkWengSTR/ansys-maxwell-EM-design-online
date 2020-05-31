def analysis_setting(oDesign, name, stoptime, timestep):
    print('Analysis params setting')

    oModule = oDesign.GetModule("AnalysisSetup")
    oModule.InsertSetup("Transient", 
        [
            "NAME:" + name,
            "Enabled:="		, True,
            "NonlinearSolverResidual:=", "0.0001",
            "TimeIntegrationMethod:=", 0,
            "StopTime:="		, stoptime,
            "TimeStep:="		, timestep,
            "OutputError:="		, False,
            "UseControlProgram:="	, False,
            "ControlProgramName:="	, " ",
            "ControlProgramArg:="	, " ",
            "CallCtrlProgAfterLastStep:=", False,
            "FastReachSteadyState:=", False,
            "IsGeneralTransient:="	, True,
            "NumberOfTimeSubDivisions:=", 1,
            "HasSweepSetup:="	, False,
            "UseAdaptiveTimeStep:="	, False,
            "InitialTimeStep:="	, "0.002s",
            "MinTimeStep:="		, "0.001s",
            "MaxTimeStep:="		, "0.003s",
            "TimeStepErrTolerance:=", 0.0001
        ])

def analysis_setting(ctx):
    print('Analysis params setting')

    oModule = ctx["ansys_object"]["oDesign"].GetModule("AnalysisSetup")

    oModule.InsertSetup("Transient",
        [
            "NAME:" + ctx["params"]["analysis_params"]["name"],
            "Enabled:="		, True,
            "NonlinearSolverResidual:=", "0.0001",
            "TimeIntegrationMethod:=", 0,
            "StopTime:="		, ctx["params"]["analysis_params"]["stoptime"],
            "TimeStep:="		, ctx["params"]["analysis_params"]["timestep"],
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

    return ctx

def start_analysis(ctx):
    print(ctx["params"]["motor_cal_params"])
    print('Start Analysis')

    ctx["data"]["opt_oModule"].SolveSetup(ctx["data"]["opt_name"])

    return ctx

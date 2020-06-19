def analysis_setting(ctx):
    print('Analysis params setting')

    oModule = ctx["ansys_object"]["oDesign"].GetModule("AnalysisSetup")
    stoptime = str(ctx["params"]["motor_cal_params"]["setting"]["cycle"]) + "/" + "(" + ctx["params"]["excitation_params"]["f_ele"] + ")"
    timestep = stoptime + "/" + str(ctx["params"]["motor_cal_params"]["setting"]["split_step"])

    oModule.InsertSetup("Transient",
        [
            "NAME:" + ctx["params"]["analysis_params"]["name"],
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

    oModule.EditSetup("setup1",
            [
                    "NAME:" + ctx["params"]["analysis_params"]["name"],
                    "Enabled:="		, True,
                    "NonlinearSolverResidual:=", "0.0001",
                    "TimeIntegrationMethod:=", 0,
                    "SmoothBHCurve:="	, False,
                    "StopTime:="		, stoptime,
                    "TimeStep:="		, timestep,
                    "OutputError:="		, False,
                    "UseControlProgram:="	, False,
                    "ControlProgramName:="	, " ",
                    "ControlProgramArg:="	, " ",
                    "CallCtrlProgAfterLastStep:=", False,
                    "FastReachSteadyState:=", False,
                    "AutoDetectSteadyState:=", False,
                    "IsGeneralTransient:="	, True,
                    "IsHalfPeriodicTransient:=", False,
                    "HasSweepSetup:="	, True,
                    "SweepSetupType:="	, "LinearStep",
                    "StartValue:="		, "0s",
                    "StopValue:="		, "10000000s",
                    "StepSize:="		, "5000000s",
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

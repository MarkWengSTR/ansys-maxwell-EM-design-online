def create_report(report_moudule, data_name, x_axis):
    report_moudule.CreateReport(data_name, "Transient", "Rectangular Plot", "Setup1 : Transient",
                         [
                             "Domain:="		, "Sweep"
                         ],
                         [
                             "Time:="		, ["All"],
                             "Dsi:="			, ["All"],
                             "Dso:="			, ["All"],
                             "slot:="		, ["All"],
                             "Hs0:="			, ["All"],
                             "Hs1:="			, ["All"],
                             "Hs2:="			, ["All"],
                             "Bs0:="			, ["All"],
                             "Bs1:="			, ["All"],
                             "Bs2:="			, ["All"],
                             "Rs:="			, ["All"],
                             "Dro:="			, ["All"],
                             "Dri:="			, ["All"],
                             "pole:="		, ["All"],
                             "rotor_type:="		, ["All"],
                             "mag_emb:="		, ["All"],
                             "mag_thick:="		, ["All"],
                             "mag_width:="		, ["All"],
                             "rotor_bridge:="	, ["All"],
                             "rotor_rib:="		, ["All"],
                             "ini_angle:="		, ["All"],
                             "speed_rpm:="		, ["All"],
                             "length:="		, ["All"],
                             "multiplier:="		, ["All"],
                             "N:="			, ["All"],
                             "Im:="			, ["All"],
                             "lead_ang:="		, ["All"]
                         ],
                         [
                             "X Component:="		, x_axis,
                             "Y Component:="		, [data_name]
                         ], [])

def report_setting(ctx):
    # report_list = {
    #     "torque": ["Moving1.Torque", "Time"],
    #     "torque_avg": ["mean(Moving1.Torque)", "Im"],
    # }

    report_moudule = ctx["ansys_object"]["oDesign"].GetModule("ReportSetup")

    for data_name, x_axis in ctx["params"]["report_list"].values():
        create_report(report_moudule, data_name, x_axis)

    ctx["data"]["report_moudule"] = report_moudule

    return ctx


def report_export(ctx):
    for report_name, data_with_x_axis in ctx["params"]["report_list"].items():
        data_name, _ = data_with_x_axis

        ctx["data"]["report_moudule"].ExportToFile(
            data_name, ctx["data"]["export_path"] + "\\" + report_name + ".csv")

    return ctx

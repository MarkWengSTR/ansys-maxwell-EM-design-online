def report_setting(oDesign, report_list):
    oModule = oDesign.GetModule("ReportSetup")

    def create_report(report_name_with_x_axis):
        report_name, x_axis = report_name_with_x_axis

        oModule.CreateReport(report_name, "Transient", "Rectangular Plot", "Setup1 : Transient",
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
                                 "Y Component:="		, [report_name]
                             ], [])

    list(map(create_report, report_list))

    return oModule

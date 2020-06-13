def band_model(ctx):
    print('Draw and set band model and ironloss')
    oEditor = ctx["ansys_object"]["oEditor"]
    oDesign = ctx["ansys_object"]["oDesign"]

    oBoundaryModule = oDesign.GetModule("BoundarySetup")
    oModelModule = oDesign.GetModule("ModelSetup")
    rotaband = ctx["params"]["name_params"]["band"]["rotaband"]
    outerband = ctx["params"]["name_params"]["band"]["outerband"]

    def iron_loss_setup():
        oBoundaryModule.SetCoreLoss(["stator", "rotor"], False)

    def outerband_edge_id_list():
        edge_list = oEditor.GetEdgeIDsFromObject(outerband)
        return [(int(edge_list[0]))]

    def draw_outer_band():
        # raduis must be named same as params setting
        oEditor.CreateCircle(
            [
                "NAME:CircleParameters",
                "IsCovered:="		, True,
                "XCenter:="		, "0mm",
                "YCenter:="		, "0mm",
                "ZCenter:="		, "0mm",
                "Radius:="		, "outer_band_D/2",
                "WhichAxis:="		, "Z",
                "NumSegments:="		, "0"
            ],
            [
                "NAME:Attributes",
                "Name:="		, outerband,
                "Flags:="		, "",
                "Color:="		, "(143 175 143)",
                "Transparency:="	, 0.8,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"vacuum\"",
                "SolveInside:="		, True
            ])

    def outer_band_setting(outerband_edge_id_list):
        oBoundaryModule.AssignVectorPotential(
            [
                "NAME:VectorPotential1",
                "Edges:="		, outerband_edge_id_list(),
                "Value:="		, "0",
                "CoordinateSystem:="	, ""
            ])

    def draw_rota_band():
        oEditor.CreateRegularPolygon(
            [
                "NAME:RegularPolygonParameters",
                "IsCovered:="		, True,
                "XCenter:="		, "0mm",
                "YCenter:="		, "0mm",
                "ZCenter:="		, "0mm",
                "XStart:="		, "rota_band_D/2",
                "YStart:="		, "0mm",
                "ZStart:="		, "0mm",
                "NumSides:="		, "360",
                "WhichAxis:="		, "Z"
            ],
            [
                "NAME:Attributes",
                "Name:="		, rotaband,
                "Flags:="		, "",
                "Color:="		, "(143 175 143)",
                "Transparency:="	, 0.8,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"vacuum\"",
                "SolveInside:="		, True
            ])

    def rota_band_setting():
        oModelModule.AssignBand(
            [
                "NAME:Data",
                "Move Type:="		, "Rotate",
                "Coordinate System:="	, "Global",
                "Axis:="		, "Z",
                "Is Positive:="		, True,
                "InitPos:="		, "ini_angle",
                "HasRotateLimit:="	, False,
                "NonCylindrical:="	, False,
                "Consider Mechanical Transient:=", False,
                "Angular Velocity:="	, "speed_rpm",
                "Objects:="		, [rotaband]
            ])

    # excute the band model and setting
    iron_loss_setup()
    draw_outer_band()
    outer_band_setting(outerband_edge_id_list)
    draw_rota_band()
    rota_band_setting()

    return ctx

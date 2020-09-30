def iron_loss_setup(band_model_ctx):
    band_model_ctx["oBoundaryModule"].SetCoreLoss(["stator", "rotor"], False)


def draw_outer_band(band_model_ctx):
    # raduis must be named same as params setting
    oEditor = band_model_ctx["oEditor"]
    outerband = band_model_ctx["outerband"]
    oEditor.CreateCircle(
        [
            "NAME:CircleParameters",
            "IsCovered:="	, True,
            "XCenter:="		, "0mm",
            "YCenter:="		, "0mm",
            "ZCenter:="		, "0mm",
            "Radius:="		, "outer_band_D/2",
            "WhichAxis:="	, "Z",
            "NumSegments:="	, "0"
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
            "SolveInside:="	, True
        ])


def outer_band_setting(band_model_ctx):
    oBoundaryModule = band_model_ctx["oBoundaryModule"]
    outerband_edge_id_list = band_model_ctx["outerband_edge_id_list"]

    oBoundaryModule.AssignVectorPotential(
        [
            "NAME:VectorPotential1",
            "Edges:="		, outerband_edge_id_list,
            "Value:="		, "0",
            "CoordinateSystem:="	, ""
        ])


def draw_rota_band(band_model_ctx):
    oEditor = band_model_ctx["oEditor"]
    rotaband = band_model_ctx["rotaband"]

    oEditor.CreateRegularPolygon(
        [
            "NAME:RegularPolygonParameters",
            "IsCovered:="	, True,
            "XCenter:="		, "0mm",
            "YCenter:="		, "0mm",
            "ZCenter:="		, "0mm",
            "XStart:="		, "rota_band_D/2",
            "YStart:="		, "0mm",
            "ZStart:="		, "0mm",
            "NumSides:="	, "360",
            "WhichAxis:="	, "Z"
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
            "SolveInside:="	, True
        ])


def rota_band_setting(band_model_ctx):
    oModelModule = band_model_ctx["oModelModule"]
    rotaband = band_model_ctx["rotaband"]

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


def band_model(ctx):
    edge_list = ctx["ansys_object"]["oEditor"].GetEdgeIDsFromObject(
        ctx["params"]["name_params"]["band"]["outerband"])

    band_model_ctx = {
        "oEditor":         ctx["ansys_object"]["oEditor"],
        "oDesign":         ctx["ansys_object"]["oDesign"],
        "oBoundaryModule": ctx["ansys_object"]["oEditor"].GetModule("BoundarySetup"),
        "oModelModule":    ctx["ansys_object"]["oDesign"].GetModule("ModelSetup"),
        "rotaband":        ctx["params"]["name_params"]["band"]["rotaband"],
        "outerband":       ctx["params"]["name_params"]["band"]["outerband"],
        "outerband_edge_id_list": (int(edge_list[0]))
    }

    print('Draw and set band model and ironloss')

    iron_loss_setup(band_model_ctx) and \
        draw_outer_band(band_model_ctx) and \
        outer_band_setting(band_model_ctx) and \
        draw_rota_band(band_model_ctx) and \
        rota_band_setting(band_model_ctx)

    return ctx

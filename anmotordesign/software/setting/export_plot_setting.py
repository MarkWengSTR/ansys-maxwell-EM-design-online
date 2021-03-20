def export_model_picture(ctx):

    fit_model_view(ctx) and \
        export_model_bmp(ctx)

    return ctx


def fit_model_view(ctx):
    ctx["ansys_object"]["oEditor"].SetModelUnits(
            [
                    "NAME:Units Parameter",
                    "Units:="		, "mm",
                    "Rescale:="		, False
            ])
    return ctx

def export_model_bmp(ctx):
    picture_path = ctx["data"]["export_path"] + "\\" + "model.bmp"

    ctx["ansys_object"]["oEditor"].ExportModelImageToFile(picture_path, 0, 0,
            [
                    "NAME:SaveImageParams",
                    "ShowAxis:="		, "True",
                    "ShowGrid:="		, "True",
                    "ShowRuler:="		, "True",
                    "ShowRegion:="		, "Default",
                    "Selections:="		, ""
            ])

    ctx["data"]["model_picture_path"] = picture_path

    return ctx

# def get_face_id(internal_ctx):
#     for object_name in internal_ctx["object_name_list"]:
#         internal_ctx["data"]["face_ids"] += [internal_ctx["oEditor"].GetFaceIDs(object_name)[0]]

#     return internal_ctx

# def create_field_plot(internal_ctx):
#     face_id_list = internal_ctx["data"]["face_ids"]

#     internal_ctx["moudule"].CreateFieldPlot(
#             [
#                     "NAME:Mag_B2",
#                     "SolutionName:="	, "setup1 : Transient",
#                     "QuantityName:="	, "Mag_B",
#                     "PlotFolder:="		, "B",
#                     "UserSpecifyName:="	, 0,
#                     "UserSpecifyFolder:="	, 0,
#                     "StreamlinePlot:="	, False,
#                     "AdjacentSidePlot:="	, False,
#                     "IntrinsicVar:="	, "Time=\'0s\'",
#                     "PlotGeomInfo:="	, [1,"Surface","FacesList"] + [len(face_id_list)] + face_id_list,
#                     "FilterBoxes:="		, [0],
#                     [
#                             "NAME:PlotOnLineSettings",
#                             [
#                                     "NAME:LineSettingsID",
#                                     "Width:="		, 4,
#                                     "Style:="		, "Cylinder"
#                             ],
#                             "IsoValType:="		, "Tone",
#                             "ArrowUniform:="	, False,
#                             "NumofArrow:="		, 100,
#                             "Refinement:="		, 0
#                     ],
#                     [
#                             "NAME:PlotOnSurfaceSettings",
#                             "Filled:="		, False,
#                             "IsoValType:="		, "Fringe",
#                             "SmoothShade:="		, True,
#                             "AddGrid:="		, False,
#                             "MapTransparency:="	, True,
#                             "Refinement:="		, 0,
#                             "Transparency:="	, 0,
#                             [
#                                     "NAME:Arrow3DSpacingSettings",
#                                     "ArrowUniform:="	, True,
#                                     "ArrowSpacing:="	, 0,
#                                     "MinArrowSpacing:="	, 0,
#                                     "MaxArrowSpacing:="	, 0
#                             ],
#                             "GridColor:="		, [255,255,255]
#                     ]
#             ], "Field")

#     return internal_ctx

# def set_field_spec(internal_ctx):
#     internal_ctx["moudule"].SetPlotFolderSettings("B",
#             [
#                     "NAME:FieldsPlotSettings",
#                     "Real time mode:="	, True,
#                     [
#                             "NAME:ColorMapSettings",
#                             "ColorMapType:="	, "Spectrum",
#                             "SpectrumType:="	, "Rainbow",
#                             "UniformColor:="	, [127,255,255],
#                             "RampColor:="		, [255,127,127]
#                     ],
#                     [
#                             "NAME:Scale3DSettings",
#                             "unit:="		, 103,
#                             "m_nLevels:="		, 10,
#                             "minvalue:="		, 0,
#                             "maxvalue:="		, 2,
#                             "log:="			, False,
#                             "IntrinsicMin:="	, 8.31690704217181E-05,
#                             "IntrinsicMax:="	, 2.23345828056335,
#                             "LimitFieldValuePrecision:=", False,
#                             "FieldValuePrecisionDigits:=", 4,
#                             "dB:="			, False,
#                             "ScaleType:="		, 1,
#                             "UserSpecifyValues:="	, internal_ctx["B_spec_value"],
#                             "ValueNumberFormatTypeAuto:=", 0,
#                             "ValueNumberFormatTypeScientific:=", False,
#                             "ValueNumberFormatWidth:=", 6,
#                             "ValueNumberFormatPrecision:=", 4
#                     ],
#                     [
#                             "NAME:Marker3DSettings",
#                             "MarkerType:="		, 9,
#                             "MarkerMapSize:="	, True,
#                             "MarkerMapColor:="	, False,
#                             "MarkerSize:="		, 0.25
#                     ],
#                     [
#                             "NAME:Arrow3DSettings",
#                             "ArrowType:="		, 1,
#                             "ArrowMapSize:="	, True,
#                             "ArrowMapColor:="	, True,
#                             "ShowArrowTail:="	, True,
#                             "ArrowSize:="		, 0.257499992847443,
#                             "ArrowMinMagnitude:="	, -0.5,
#                             "ArrowMaxMagnitude:="	, 2.56404,
#                             "ArrowMagnitudeThreshold:=", 0,
#                             "ArrowMagnitudeFilteringFlag:=", False,
#                             "ArrowMinIntrinsicMagnitude:=", 0,
#                             "ArrowMaxIntrinsicMagnitude:=", 1
#                     ],
#                     [
#                             "NAME:DeformScaleSettings",
#                             "ShowDeformation:="	, True,
#                             "MinScaleFactor:="	, 0,
#                             "MaxScaleFactor:="	, 1,
#                             "DeformationScale:="	, 0
#                     ]
#             ])

#     return internal_ctx





# def export_flux_density(ctx):
#     name_params = ctx["params"]["name_params"]

#     internal_ctx = {
#         "path": ctx["data"]["export_path"] + "\\" + "flux_density.bmp",
#         "oEditor": ctx["ansys_object"]["oEditor"],
#         "moudule": ctx["ansys_object"]["oDesign"].GetModule("FieldsReporter"),
#         "object_name_list": ctx["data"]["coil_name_list"] + ctx["data"]["mag_name_list"] + [name_params["stator"], name_params["rotor"], name_params["band"]["rotaband"], name_params["band"]["outerband"]],
#         "B_spec_value": [11, 0, 0.2 , 0.4 , 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2],
#         "data": {
#             "face_ids": [],
#         }
#     }

#     get_face_id(internal_ctx) and \
#         create_field_plot(internal_ctx) and \
#         set_field_spec(internal_ctx) and \
#         export_field_bmp(internal_ctx)

#     print(internal_ctx)

#     return ctx

# export_flux_density({})
    # internal_ctx = {
    #     "path": "./flux_density.bmp",
    #     "oEditor": oEditor,
    #     "moudule": oDesign.GetModule("FieldsReporter"),
    #     "object_name_list": ['Ain1', 'Aout1', 'Aout2', 'Ain2', 'Bout1', 'Bin1', 'Bin2', 'Bout2', 'Cin1', 'Cout1', 'Cout2', 'Cin2', 'Aout3', 'Ain3', 'Ain4', 'Aout4', 'Bin3', 'Bout3', 'Bout4', 'Bin4', 'Cout3', 'Cin3', 'Cin4', 'Cout4', 'magnet', 'magnet_1', 'magnet_2', 'magnet_3', 'magnet_4', 'magnet_5', 'magnet_6', 'magnet_7', 'magnet_8', 'magnet_9', 'stator', 'rotor', 'rotaband', 'outerband'],
    #     "B_spec_value": [11, 0, 0.2 , 0.4 , 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2],
    #     "data": {
    #         "face_ids": [],
    #     }
    # }


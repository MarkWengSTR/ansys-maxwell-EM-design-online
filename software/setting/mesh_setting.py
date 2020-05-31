def mesh_setting(oDesign, band_name_list):
    print('Set Mesh')

    oModule = oDesign.GetModule("MeshSetup")
    rotaband, outerband = band_name_list

    oModule.AssignLengthOp(
            [
                    "NAME:mesh",
                    "RefineInside:="	, True,
                    "Enabled:="		, True,
                    "Objects:="		, [rotaband],
                    "RestrictElem:="	, False,
                    "NumMaxElem:="		, "1000",
                    "RestrictLength:="	, True,
                    "MaxLength:="		, "0.5mm"
            ])

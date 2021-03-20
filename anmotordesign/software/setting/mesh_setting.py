def mesh_setting(ctx):
    print('Set Mesh')

    oModule = ctx["ansys_object"]["oDesign"].GetModule("MeshSetup")

    oModule.AssignLengthOp(
            [
                    "NAME:mesh",
                    "RefineInside:="	, True,
                    "Enabled:="		, True,
                    "Objects:="		, [ctx["params"]["name_params"]["band"]["rotaband"]],
                    "RestrictElem:="	, False,
                    "NumMaxElem:="		, "1000",
                    "RestrictLength:="	, True,
                    "MaxLength:="		, "0.5mm"
            ])

    return ctx

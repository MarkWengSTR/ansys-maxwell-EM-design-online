# python & ansoft connection

from win32com import client
import os


def find_or_initial_project():
    print('Initial project')

    # import ipdb; ipdb.set_trace()
    oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")

    oDesktop = oAnsoftApp.GetAppDesktop()
    oProject = oDesktop.NewProject()
    # project
    # if len(oDesktop.GetProjects()) == 0:
    #     oProject = oDesktop.NewProject()
    # else:
    #     oProject = oDesktop.GetActiveProject()

    oDesign = oProject.InsertDesign(
        "Maxwell 2D", "Maxwell2DDesign1", "Transient", "")
    # find previous project
    # if len(oProject.GetTopDesignList()) == 0:
    #     oDesign = oProject.InsertDesign("Maxwell 2D", "Maxwell2DDesign1", "Transient", "")
    # else:
    #     oDesign = oProject.GetActiveDesign()

    oEditor = oDesign.SetActiveEditor("3D Modeler")

    ansys_object = {
        "oProject": oProject,
        "oDesign": oDesign,
        "oEditor": oEditor,
    }

    return ansys_object

def save_project(ctx):
    export_path = ctx["data"]["export_path"]
    time_stamp = ctx["data"]["time_stamp"]

    if not os.path.isdir(export_path):
        os.mkdir(export_path)

    ctx["ansys_object"]["oProject"].SaveAs(export_path + "\\" + "project" + "_" + time_stamp + ".aedt", True)

    return ctx

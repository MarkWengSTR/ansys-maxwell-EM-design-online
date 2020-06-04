from params.stator import stator_params
from params.rotor import rotor_params
from params.motor import motor_params
from params.excitation import excitation_params
from params.band import band_params
from params.name import name_dirt
from params.analysis import analysis_params
from params.optiparametric import optiparametric_variables
from params.report import report_list

from software.project.ansys_python_interface import find_or_initial_project

# import ipdb; ipdb.set_trace()
# from params.geometry_params_checking import geometry_params_checking
from software.setting.params_setting import params_setting

from software.model.stator_model import stator_model
from software.model.rotor_model import rotor_model
from software.model.band_model import band_model
from software.model.magnets_model import magnets_model
from software.model.coils_model import coils_model

from software.setting.current_excitation_setting import current_excitation_setting
from software.setting.model_setting import model_setting
from software.setting.mesh_setting import mesh_setting
from software.setting.analysis_setting import analysis_setting
from software.setting.optimetrics_setting import optimetrics_setting
from software.setting.report_setting import report_setting


if __name__ == "__main__":
    # geomotry_errors = geometry_params_checking({**stator_params, **rotor_params})

    # if geomotry_errors['error_present?']:
    #     raise BaseException(geomotry_errors['error_msg'])

    total_mech_params = {**stator_params, **rotor_params,
                         **motor_params, **band_params, **excitation_params}

    oProject, oDesign, oEditor = find_or_initial_project()

    params_setting(oDesign, total_mech_params)

    stator_model(oEditor, stator_params)

    rotor_model(oEditor, rotor_params)

    magnets_model(oEditor, rotor_params)

    coil_name_list = coils_model(oEditor, int(stator_params["slot"]))

    current_excitation_setting(oDesign, coil_name_list,
                               name_dirt["excitation_name"])

    model_setting(oDesign, motor_params["length"], motor_params["multiplier"])

    band_model(oDesign, oEditor, name_dirt["band_name"])

    mesh_setting(oDesign, name_dirt["band_name"])

    analysis_setting(oDesign, analysis_params["name"],
                     analysis_params["stoptime"], analysis_params["timestep"])

    oModule = oDesign.GetModule("BoundarySetup")
    oModule.SetCoreLoss(["stator", "rotor"], False)

    print('Start Analysis')

    opt_oModule, opt_name = optimetrics_setting(
        oProject, oDesign, optiparametric_variables, analysis_params["name"])

    opt_oModule.SolveSetup(opt_name)

    report_moudule = report_setting(oDesign, report_list, optiparametric_variables)

    # TODO: this path should be general
    report_moudule.ExportToFile(
        "Moving1.Torque", "C:/Users/bskin/Desktop/Ansoft_script/torque.csv")

    print('Simulation Completed')

from params.mechanical import stator_params, rotor_params
from params.motor import motor_params
from params.excitation import excitation_params
from params.band import band_params
from params.name import name_params
from params.analysis import analysis_params
from params.optiparametric import optiparametric_variables
from params.report import report_list

from software.project.ansys_python_interface import find_or_initial_project

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

# import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    # geomotry_errors = geometry_params_checking({**stator_params, **rotor_params})

    # if geomotry_errors['error_present?']:
    #     raise BaseException(geomotry_errors['error_msg'])

    total_mech_params = {**rotor_params, **stator_params,
                         **motor_params, **band_params, **excitation_params}

    ansys_object = find_or_initial_project()

    params_setting(ansys_object["oDesign"], total_mech_params)

    stator_model(ansys_object["oEditor"], stator_params)

    rotor_model(ansys_object["oEditor"], rotor_params)

    magnets_model(ansys_object["oEditor"], rotor_params)

    coil_name_list = coils_model(ansys_object["oEditor"], int(stator_params["slot"]))

    current_excitation_setting(ansys_object["oDesign"], coil_name_list,
                               name_params["excitation_name"])

    model_setting(ansys_object["oDesign"], motor_params["length"], motor_params["multiplier"])

    band_model(ansys_object, name_params["band_name"])

    mesh_setting(ansys_object["oDesign"], name_params["band_name"])

    analysis_setting(ansys_object["oDesign"], analysis_params["name"],
                     analysis_params["stoptime"], analysis_params["timestep"])

    print('Start Analysis')

    opt_oModule, opt_name = optimetrics_setting(
        ansys_object["oProject"], ansys_object["oDesign"], optiparametric_variables, analysis_params["name"])

    opt_oModule.SolveSetup(opt_name)

    report_moudule = report_setting(ansys_object["oDesign"], report_list, optiparametric_variables)

    # TODO: this path should be general
    report_moudule.ExportToFile(
        "Moving1.Torque", "./torque.csv")

    print('Simulation Completed')

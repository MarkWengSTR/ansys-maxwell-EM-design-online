import os

from params.total_params_calculation import total_params_calculate

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

    # params = {
    # "spec_params": spec_params,
    # "motor_cal_params": motor_cal_params,
    # "stator_params": stator_params,
    # "rotor_params": rotor_params,
    # "motor_params": motor_params,
    # "excitation_params": excitation_params,
    # "band_params": band_params,
    # "name_params": name_params,
    # "analysis_params": analysis_params,
    # "optiparametric_params": optiparametric_params,
    # "report": report_list,
    # }

    # ansys_object = {
    #     "oProject": oProject,
    #     "oDesign": oDesign,
    #     "oEditor": oEditor,
    # }

    ctx = {
        "params": total_params_calculate(),
        "ansys_object": find_or_initial_project(),
        "coil_name_list": None
    }

    params_setting(ctx) and \
        stator_model(ctx) and \
        rotor_model(ctx) and \
        magnets_model(ctx) and \
        coils_model(ctx)

    current_excitation_setting(ansys_object["oDesign"], coil_name_list,
                               total_params["name_params"]["excitation_name"])

    model_setting(ansys_object["oDesign"], total_params["motor_params"]["length"], total_params["motor_params"]["multiplier"])

    band_model(ansys_object, total_params["name_params"]["band_name"])

    mesh_setting(ansys_object["oDesign"], total_params["name_params"]["band_name"])

    analysis_setting(ansys_object["oDesign"], total_params["analysis_params"]["name"],
                     total_params["analysis_params"]["stoptime"], total_params["analysis_params"]["timestep"])

    print(total_params["motor_cal_params"]["calculation"])
    print('Start Analysis')

    opt_oModule, opt_name = optimetrics_setting(
        ansys_object["oProject"], ansys_object["oDesign"], total_params)

    opt_oModule.SolveSetup(opt_name)

    report_moudule = report_setting(ansys_object["oDesign"], total_params["report"])

    report_moudule.ExportToFile(
        "Moving1.Torque", os.path.join(os.getcwd(), "tmp", "torque.csv"))

    print('Simulation Completed')

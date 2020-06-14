import os
import datetime
import time

# params
from params.motor_params import motor_cal_params
from params.ansys_params import stator_params, rotor_params, other_motor_params, excitation_params, band_params, name_params, analysis_params, optiparametric_params, report_list
from params.total_params_calculation import total_params_calculate

# project
from software.project.ansys_python_interface import find_or_initial_project, save_project

# modeling
from software.model.stator_model import stator_model
from software.model.rotor_model import rotor_model
from software.model.band_model import band_model
from software.model.magnets_model import magnets_model
from software.model.coils_model import coils_model

# setting
from software.setting.params_setting import params_setting
from software.setting.current_excitation_setting import current_excitation_setting
from software.setting.model_setting import model_setting
from software.setting.mesh_setting import mesh_setting
from software.setting.analysis_setting import analysis_setting, start_analysis
from software.setting.optimetrics_setting import optimetrics_setting
from software.setting.report_setting import report_setting, report_export

# other
# import ipdb; ipdb.set_trace()
# from params.geometry_params_checking import geometry_params_checking
# geomotry_errors = geometry_params_checking({**stator_params, **rotor_params})

# if geomotry_errors['error_present?']:
#     raise BaseException(geomotry_errors['error_msg'])

spec_params = {
    "stator_OD_limit":  120,
    "max_power":        5000,
    "voltage_dc":       48,
    "max_torque_nm":    27,
    "max_speed_rpm":    5000,
    "error_present":    False,
    "error_msg":        None,
}


def run_ansys(spec):
    time_stamp = str(int(time.mktime(datetime.datetime.now().timetuple())))

    ctx = {
        "params": {
            "spec_params": spec_params,
            "motor_cal_params": motor_cal_params,
            "stator_params": stator_params,
            "rotor_params": rotor_params,
            "other_motor_params": other_motor_params,
            "excitation_params": excitation_params,
            "band_params": band_params,
            "name_params": name_params,
            "analysis_params": analysis_params,
            "optiparametric_params": optiparametric_params,
            "report_list": report_list,
        },
        "ansys_object": {
            "oProject": None,
            "oDesign": None,
            "oEditor": None,
        },
        "data": {
            "coil_name_list": None,
            "opt_name": "OPT",
            "opt_oModule": None,
            "report_moudule": None,
            "time_stamp": time_stamp,
            "export_path": os.path.join(os.getcwd(), "tmp", str(datetime.date.today()).replace("-", "_") + "_" + time_stamp),
        }
    }

    total_params_calculate(ctx) and \
        find_or_initial_project(ctx) and \
        params_setting(ctx) and \
        stator_model(ctx) and \
        rotor_model(ctx) and \
        magnets_model(ctx) and \
        coils_model(ctx) and \
        current_excitation_setting(ctx) and \
        model_setting(ctx) and \
        band_model(ctx) and \
        mesh_setting(ctx) and \
        analysis_setting(ctx) and \
        optimetrics_setting(ctx) and \
        save_project(ctx) and \
        report_setting(ctx) and \
        start_analysis(ctx) and \
        report_export(ctx)

    print('Simulation Completed')

    return ctx["params"]["motor_cal_params"]


if __name__ == "__main__":
    run_ansys({"call": "just for test"})

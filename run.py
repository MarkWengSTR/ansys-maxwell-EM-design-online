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
from software.setting.material_setting import material_setting
from software.setting.analysis_setting import analysis_setting, start_analysis
from software.setting.optimetrics_setting import optimetrics_setting
from software.setting.report_setting import report_setting, report_export
from software.setting.export_plot_setting import export_model_picture

# postprocess
from postprocess.result import result_process

# debug
# import ipdb; ipdb.set_trace()
# from win32com import client
# oAnsoftApp = client.Dispatch("Ansoft.ElectronicsDesktop")
# oDesktop = oAnsoftApp.GetAppDesktop()
# oProject = oDesktop.SetActiveProject("project_1592523833")
# oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
# oEditor = oDesign.SetActiveEditor("3D Modeler")

# other
# from params.geometry_params_checking import geometry_params_checking
# geomotry_errors = geometry_params_checking({**stator_params, **rotor_params})

# if geomotry_errors['error_present?']:
#     raise BaseException(geomotry_errors['error_msg'])

spec_params = {
    "stator_OD_limit": 120,
    "max_power":       5000,
    "voltage_dc":      48,
    "max_torque_nm":   27,
    "max_speed_rpm":   5000,
    "export_path":     None,
    "pj_key": None,
    "res_url": None,
}


def run_ansys(ctx):
    spec = {**spec_params, **ctx["request"]}

    # time_stamp = str(int(time.mktime(datetime.datetime.now().timetuple())))
    time_stamp = str(spec["pj_key"])
    project_name = str(datetime.date.today()).replace("-", "_") + "_" + time_stamp

    ctx = {
        **ctx,
        "params": {
            "spec_params": spec,
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
            "project_name": project_name,
            "coil_name_list": [],
            "mag_name_list": [],
            "opt_name": "OPT",
            "opt_oModule": None,
            "report_moudule": None,
            "time_stamp": time_stamp,
            "export_path": spec["export_path"] or os.path.join(os.getcwd(), "tmp", project_name),
            "model_picture_path": None,
        },
        "response": {
            "model_picture_path": None,
            "stator_OD": None,
            "motor_length": None,
            "ele_ang_x_axis": [],
            "corner_point": {
                "current": None,
                "speed": None,
                "torque_data": [],
                "avg_torque": None,
                "torque_ripple": None,
                "line_voltage_rms": None,
                "core_loss": None,
                "core_loss_factor": None,
                "copper_loss": None,
                "efficiency": None,
                "output_power": None,
                "current_density": None,
            },
            "noload": {
                "ph_voltage_data": [],
                "cogging_data": [],
                "ph_voltage_rms": None,
                "cogging": None,
                "speed": 1000,
            },
            "max_speed": {
                "line_voltage_rms": None,
                "speed": None,
            },
            "material_name": {
                "stator": None,
                "rotor": None,
                "magnet": None
            }
        }
    }

    total_params_calculate(ctx) and \
        find_or_initial_project(ctx) and \
        save_project(ctx) and \
        params_setting(ctx) and \
        material_setting(ctx) and \
        stator_model(ctx) and \
        rotor_model(ctx) and \
        magnets_model(ctx) and \
        coils_model(ctx) and \
        export_model_picture(ctx) and \
        current_excitation_setting(ctx) and \
        model_setting(ctx) and \
        band_model(ctx) and \
        mesh_setting(ctx) and \
        analysis_setting(ctx) and \
        optimetrics_setting(ctx) and \
        report_setting(ctx) and \
        start_analysis(ctx) and \
        report_export(ctx) and \
        result_process(ctx)

    print(ctx["response"])
    print('Simulation Completed')

    # ctx["response"] = ctx["params"]["motor_cal_params"]

    return ctx


if __name__ == "__main__":
    run_ansys({"request": {"call": "just for test"}})

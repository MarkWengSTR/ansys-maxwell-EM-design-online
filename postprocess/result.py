import pandas as pd
import numpy as np
import os


def result_process(ctx):
    result_ctx = {
        "data_path": ctx["data"]["export_path"],
        "total_step": ctx["params"]["motor_cal_params"]["setting"]["cycle"] * ctx["params"]["motor_cal_params"]["setting"]["split_step"],
        "data": {
            "ele_ang_x_axis": [],
            "corner_point": {
                "current": ctx["params"]["motor_cal_params"]["max_current_rms"],
                "speed": ctx["params"]["motor_cal_params"]["corner_speed_rpm"],
                "torque_data": [],
                "avg_torque": None,
                "torque_ripple": None,
                "line_voltage_rms": None,
                "core_loss_x1": None,
                "copper_loss": None,
                "efficiency": None,
                "output_power": None,
                "model_picture_path": ctx["data"]["model_picture_path"],
                "current density": ctx["params"]["motor_cal_params"]["estimate"]["max_J"],
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
                "speed": ctx["params"]["motor_cal_params"]["max_speed_rpm"],
            }
        }
    }

    prepare_x_axis_ele_ang(result_ctx) and \
        process_toruqe(result_ctx)

    ctx["response"] = {**ctx["response"], **result_ctx["data"]}

    return ctx

def prepare_x_axis_ele_ang(result_ctx):
    step_ang = 360 / result_ctx["data"]["total_step"]

    result_ctx["data"]["ele_ang_x_axis"] = np.arange(0, 360 + step_ang, step_ang).tolist()

    return result_ctx


def process_toruqe(result_ctx):
    tq_df = pd.read_csv(os.path.join(os.getcwd(), "tmp",
                                     "2020_06_19_1592578043", "torque.csv"))

    cogging_data_arr = tq_df.filter(like="0A").filter(
        like= str(result_ctx["data"]["noload"]["speed"]) + "rpm").dropna().values.flatten()
    torque_data_arr = tq_df.filter(like = str(result_ctx["data"]["corner_point"]["current"]) + "A").filter(
        like = str(result_ctx["data"]["corner_point"]["speed"]) + "rpm").dropna().values.flatten()

    result_ctx["data"]["noload"]["cogging_data"] = cogging_data_arr.tolist()
    result_ctx["data"]["noload"]["cogging"] =  cogging_data_arr.max() - cogging_data_arr.min()

    result_ctx["data"]["corner_point"]["torque_data"] = torque_data_arr.tolist()
    result_ctx["data"]["corner_point"]["avg_torque"] = torque_data_arr.mean()
    result_ctx["data"]["corner_point"]["torque_ripple"] = (torque_data_arr.max() - torque_data_arr.min()) / torque_data_arr.mean() * 100

    return result_ctx


# result_ctx = {
#     "data": {
#         "ele_ang_x_axis": [],
#         "total_step": 50,
#         "corner_point": {
#             "current": 297,
#             "speed": 1769,
#             "torque_data": [],
#             "avg_torque": None,
#             "torque_ripple": None,
#             "line_voltage_rms": None,
#             "core_loss_x1": None,
#             "copper_loss": None,
#             "efficiency": None,
#             "output_power": None,
#             "model_picture_path": None,
#             "current density": None,
#         },
#         "noload": {
#             "ph_voltage_data": [],
#             "cogging_data": [],
#             "ph_voltage_rms": None,
#             "cogging": None,
#             "speed": 1000,
#         },
#         "max_speed": {
#             "line_voltage_rms": None,
#             "speed": 5000,
#         }
#     }
# }
# process_toruqe(result_ctx)
# import ipdb; ipdb.set_trace()


import math
import os

import numpy as np
import pandas as pd


def np_rms(arr):
    return np.sqrt((arr ** 2).sum() / arr.size)


def result_process(ctx):
    motor_cal_params = ctx["params"]["motor_cal_params"]
    result_ctx = {
        "data_path": ctx["data"]["export_path"],
        "total_step": motor_cal_params["setting"]["cycle"] * motor_cal_params["setting"]["split_step"],
        "data": {
            "copper": {
                "temp": 30,
                "slot_distance": (motor_cal_params["calculation"]["est_stator_OD"] + motor_cal_params["calculation"]["est_rotor_OD"]) * math.pi / (2 * motor_cal_params["stator"]["slot"]),
                "coil_cross_slot_num": math.floor(motor_cal_params["stator"]["slot"] / motor_cal_params["rotor"]["pole"]),
                "motor_length": motor_cal_params["length"],
                "coil_turns": motor_cal_params["calculation"]["coil_turns"],
                "para_conductor": motor_cal_params["calculation"]["para_conductor"],
                "conductor_OD": motor_cal_params["coil"]["conductor_OD"],
                "y_para": motor_cal_params["coil"]["y_para"],
                "copper_ele_resistivity": 1/58,
                "correct_ratio": 1.2,
            },
        },
        "result": {
            "model_picture_path": ctx["data"]["model_picture_path"],
            "ele_ang_x_axis": [],
            "stator_OD": motor_cal_params["calculation"]["est_stator_OD"],
            "motor_length": motor_cal_params["length"],
            "coil_turn": motor_cal_params["calculation"]["coil_turns"],
            "corner_point": {
                "current": motor_cal_params["max_current_rms"],
                "speed": motor_cal_params["corner_speed_rpm"],
                "torque_data": [],
                "avg_torque": None,
                "torque_ripple": None,
                "line_voltage_rms": None,
                "core_loss": None,
                "core_loss_factor": motor_cal_params["core_loss_factor"],
                "copper_loss": None,
                "efficiency": None,
                "output_power": None,
                "current_density": motor_cal_params["estimate"]["max_J"],
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
                "speed": motor_cal_params["max_speed_rpm"],
            },
            "material_name": {
                "stator": ctx["params"]["motor_cal_params"]["material"]["stator"].replace("\"", "").replace("_steel", ""),
                "rotor": ctx["params"]["motor_cal_params"]["material"]["rotor"].replace("\"", "").replace("_steel", ""),
                "magnet": ctx["params"]["motor_cal_params"]["material"]["magnet"].replace("\"", "").replace("_mag", "")
            }
        }
    }

    prepare_x_axis_ele_ang(result_ctx) and \
        process_toruqe(result_ctx) and \
        process_voltage(result_ctx) and \
        process_core_loss(result_ctx) and \
        process_copper_loss(result_ctx) and \
        process_efficiency(result_ctx)

    ctx["response"] = {**ctx["response"], **result_ctx["result"]}

    return ctx


def prepare_x_axis_ele_ang(result_ctx):
    step_ang = 360 / result_ctx["total_step"]

    result_ctx["result"]["ele_ang_x_axis"] = np.arange(
        0, 360 + step_ang, step_ang).tolist()

    return result_ctx


def process_toruqe(result_ctx):
    tq_df = pd.read_csv(os.path.join(result_ctx["data_path"], "torque.csv"))
    noload_speed = result_ctx["result"]["noload"]["speed"]
    corner_current = result_ctx["result"]["corner_point"]["current"]
    corner_speed = result_ctx["result"]["corner_point"]["speed"]

    cogging_data_arr = tq_df.filter(like="0A").filter(
        like=str(noload_speed) + "rpm").dropna().values.flatten()
    torque_data_arr = tq_df.filter(like=str(corner_current) + "A").filter(
        like=str(corner_speed) + "rpm").dropna().values.flatten()

    result_ctx["result"]["noload"]["cogging_data"] = cogging_data_arr.tolist()
    result_ctx["result"]["noload"]["cogging"] = cogging_data_arr.max() - \
        cogging_data_arr.min()

    result_ctx["result"]["corner_point"]["torque_data"] = torque_data_arr.tolist()
    result_ctx["result"]["corner_point"]["avg_torque"] = torque_data_arr.mean()
    result_ctx["result"]["corner_point"]["torque_ripple"] = (
        torque_data_arr.max() - torque_data_arr.min()) / torque_data_arr.mean() * 100

    return result_ctx


def process_voltage(result_ctx):
    vol_ph = pd.read_csv(os.path.join(
        result_ctx["data_path"], "voltage_ph.csv"))
    vol_line = pd.read_csv(os.path.join(
        result_ctx["data_path"], "voltage_line.csv"))
    noload_speed = result_ctx["result"]["noload"]["speed"]
    corner_current = result_ctx["result"]["corner_point"]["current"]
    corner_speed = result_ctx["result"]["corner_point"]["speed"]
    max_speed = result_ctx["result"]["max_speed"]["speed"]

    bemf_ph_data_arr = vol_ph.filter(like="0A").filter(
        like=str(noload_speed) + "rpm").dropna().values.flatten()
    bemf_line_data_arr = vol_line.filter(like="0A").filter(
        like=str(noload_speed) + "rpm").dropna().values.flatten()
    cor_vol_data_arr = vol_line.filter(like=str(corner_current) + "A").filter(
        like=str(corner_speed) + "rpm").dropna().values.flatten()

    result_ctx["result"]["noload"]["ph_voltage_data"] = bemf_ph_data_arr.tolist()
    result_ctx["result"]["noload"]["ph_voltage_rms"] = np_rms(bemf_ph_data_arr)
    result_ctx["result"]["max_speed"]["line_voltage_rms"] = np_rms(
        bemf_line_data_arr) * (max_speed / noload_speed)
    result_ctx["result"]["corner_point"]["line_voltage_rms"] = np_rms(
        cor_vol_data_arr)

    return result_ctx


def process_core_loss(result_ctx):
    core_loss = pd.read_csv(os.path.join(
        result_ctx["data_path"], "coreloss.csv"))
    corner_current = result_ctx["result"]["corner_point"]["current"]
    corner_speed = result_ctx["result"]["corner_point"]["speed"]

    cor_core_loss_data_arr = core_loss.filter(like=str(corner_current) + "A").filter(
        like=str(corner_speed) + "rpm").dropna().values.flatten()

    result_ctx["result"]["corner_point"]["core_loss"] = cor_core_loss_data_arr[-5:].mean()

    return result_ctx


def process_copper_loss(result_ctx):
    corner_current = result_ctx["result"]["corner_point"]["current"]
    copper_data = result_ctx["data"]["copper"]

    slot_distance = copper_data["slot_distance"]
    coil_cross_slot_num = copper_data["coil_cross_slot_num"]
    coil_turns = copper_data["coil_turns"]
    para_conductor = copper_data["para_conductor"]
    conductor_OD = copper_data["conductor_OD"]
    copper_ele_resistivity = copper_data["copper_ele_resistivity"]
    motor_length = copper_data["motor_length"]
    temp = copper_data["temp"]
    correct_ratio = copper_data["correct_ratio"]
    y_para = copper_data["y_para"]

    single_coil_dist = slot_distance * coil_cross_slot_num * math.pi + motor_length * 2
    single_coil_resis = copper_ele_resistivity * \
        (1 / (conductor_OD**2 * math.pi/4 * 1000)) * \
        single_coil_dist * coil_turns / para_conductor
    total_coil_resis = single_coil_resis * correct_ratio / y_para
    resis_with_temp = total_coil_resis * (1 + 0.004 * (temp - 20))

    result_ctx["result"]["corner_point"]["copper_loss"] = 3 * \
        corner_current ** 2 * resis_with_temp

    return result_ctx


def process_efficiency(result_ctx):
    corner_point = result_ctx["result"]["corner_point"]
    torque = corner_point["avg_torque"]
    speed = corner_point["speed"]
    core_loss = corner_point["core_loss"] * corner_point["core_loss_factor"]
    copper_loss = corner_point["copper_loss"]

    output_power = torque * speed * 2 * math.pi / 60
    efficiency = output_power / (output_power + core_loss + copper_loss)

    result_ctx["result"]["corner_point"]["output_power"] = output_power
    result_ctx["result"]["corner_point"]["efficiency"] = round(
        efficiency * 100, 2)

    return result_ctx

# import ipdb; ipdb.set_trace()
# result_ctx = {
#     "data_path": os.path.join(os.getcwd(), "tmp", "2020_06_21_1592743691"),
#     "total_step": 50,
#     "data": {
#         "copper": {
#             "temp": 30,
#             "slot_distance": 21.2319,
#             "coil_cross_slot_num": 1,
#             "motor_length": 96,
#             "coil_turns": 2,
#             "para_conductor": 18,
#             "conductor_OD": 1,
#             "y_para": 1,
#             "copper_ele_resistivity": 1/58,
#             "correct_ratio": 1.2,
#         },
#     },
#     "result": {
#         "model_picture_path": None,
#         "ele_ang_x_axis": [],
    # "stator_OD": 110,
    # "motor_length": 50,
    # "coil_turn": 2,
#         "corner_point": {
#             "current": 297,
#             "speed": 1769,
#             "torque_data": [],
#             "avg_torque": None,
#             "torque_ripple": None,
#             "line_voltage_rms": None,
#             "core_loss": None,
#             "core_loss_factor": 1,
#             "copper_loss": None,
#             "efficiency": None,
#             "output_power": None,
#             "current_density": None,
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
#         },
#         "material_name": {
#             "stator": None,
#             "rotor": None,
#             "magnet": None
#         }
#     }
# }

# prepare_x_axis_ele_ang(result_ctx) and \
#     process_toruqe(result_ctx) and \
#     process_voltage(result_ctx) and \
#     process_core_loss(result_ctx) and \
#     process_copper_loss(result_ctx) and \
#     process_efficiency(result_ctx)

import math

spec_params = {
    "out_power":      1000,
    "voltage_dc":     48,
    "voltage_buffer": 0.9,
    "est_pf":         0.95,
    "est_eff":        0.95,
    "speed_rpm":      3300,
    "speed_rad_s":    None,
    "current_rms":    None,
    "torque_nm":      None,
    "ke":             None,
    "kt":             None,
    "error_present":  False,
    "error_msg":      None,
}

motor_cal_parms = {
    "stator": {
        "OD_limit": 110,
        "slot": 12,
        "shoes_height_front": 1,
        "shoes_height_back": 1,
        "slot_corner_arc": 0.5,
    },
    "rotor": {
        "pole": 10,
        "mag_emb": 0.8,  # easier magetization
        "mag_pc": 7.5,  # for not easy to broke
    },
    "length": 50,
    "airgap": 0.5,
    "w_factor_10p12s": 0.933,
    "estimate": {
        "teeth_mag_ang_ratio": 0.6,
        "york_teeth_ratio": 0.7,
        "rotor_OD_ratio": 0.6,
        "Bg": 1.2,
    },
    "coil": {
        "conductor_OD": 1,
        "Y_para": 1,
        "membrane_ratio": 1.075,
    },
    "calculation": {
        "est_rotor_OD": None,
        "mag_thick": None,
        "teeth_width": None,
        "york_width": None,
        "slot_height": None,
        "slot_width_front": None,
        "slot_width_back": None,
        "conductor_para": None,
        "coil_turns": None,
    },
}

total_cal_params = {"spec_params": spec_params,
                    "motor_cal_parms": motor_cal_parms}


def ktke_validate(total_cal_params):
    spec_params = total_cal_params["spec_params"]

    out_power, voltage_dc, voltage_buffer, est_pf, est_eff, speed_rpm = \
        spec_params["out_power"], spec_params["voltage_dc"], spec_params[
            "voltage_buffer"], spec_params["est_pf"], spec_params["est_eff"], spec_params["speed_rpm"]

    spec_params["speed_rad_s"] = round((speed_rpm * 2 * math.pi) / 60, 2)
    spec_params["current_rms"] = round(
        (out_power / est_eff) / (3**0.5 * (voltage_dc * voltage_buffer / 2**0.5) * est_pf), 2)
    spec_params["torque_nm"] = round(out_power / spec_params["speed_rad_s"], 2)

    spec_params["ke"] = round(
        (voltage_dc * voltage_buffer / 3**0.5) / spec_params["speed_rad_s"], 4)
    spec_params["kt"] = round(
        spec_params["torque_nm"] / (1.5 * spec_params["current_rms"] * 2**0.5), 4)

    if spec_params["kt"] > spec_params["ke"]:
        spec_params["error_present"] = True
        spec_params["error_msg"] = "ke must large than kt"

    return total_cal_params


def expend_NBLR(total_cal_params):
    cal_parms = total_cal_params["motor_cal_parms"]

    ke = total_cal_params["spec_params"]["ke"]
    stator_OD_limit, slot = cal_parms["stator"]["OD_limit"] / \
        1000,        cal_parms["stator"]["slot"]
    Bg = cal_parms["estimate"]["Bg"]
    rotor_OD_ratio = cal_parms["estimate"]["rotor_OD_ratio"]
    length = cal_parms["length"] / 1000
    w_factor_10p12s = cal_parms["w_factor_10p12s"]
    Y_para = cal_parms["coil"]["Y_para"]

    coil_turns = math.ceil(
        ke/(2 * (slot / 3 / Y_para) * Bg * length * (stator_OD_limit * rotor_OD_ratio / 2) * w_factor_10p12s))

    est_rotor_ORad = round(
        ke/(2 * (coil_turns * slot / 3 / Y_para) * Bg * length * w_factor_10p12s), 3)

    cal_parms["calculation"]["est_rotor_OD"] = est_rotor_ORad * 2 * 1000
    cal_parms["calculation"]["coil_turns"] = coil_turns

    return total_cal_params


def expend_stator_teeth_york(total_cal_params):
    cal_parms = total_cal_params["motor_cal_parms"]

    teeth_mag_ang_ratio = cal_parms["estimate"]["teeth_mag_ang_ratio"]
    pole = cal_parms["rotor"]["pole"]
    mag_emb = cal_parms["rotor"]["mag_emb"]
    york_teeth_ratio = cal_parms["estimate"]["york_teeth_ratio"]
    rotor_OD = cal_parms["calculation"]["est_rotor_OD"]
    airgap = cal_parms["airgap"]
    shoes_height_front = cal_parms["stator"]["shoes_height_front"]
    shoes_height_back = cal_parms["stator"]["shoes_height_back"]

    mag_angle = mag_emb * (360 / pole)
    teeth_angle = teeth_mag_ang_ratio * mag_angle

    teeth_width = round((rotor_OD + (airgap + shoes_height_front +
                                     shoes_height_back)*2) * math.pi * (teeth_angle / 360), 1)
    york_width = round(teeth_width * york_teeth_ratio, 1)

    cal_parms["calculation"]["teeth_width"] = teeth_width
    cal_parms["calculation"]["york_width"] = york_width

    return total_cal_params


def mech_cal(total_cal_params):
    ktke_validate(total_cal_params) and \
        expend_NBLR(total_cal_params) and \
        expend_stator_teeth_york(total_cal_params)

    if total_cal_params["spec_params"]["error_present"]:
        raise BaseException(total_cal_params["spec_params"]["error_msg"])


mech_cal(total_cal_params)

# import ipdb; ipdb.set_trace()
# ktke_validate(total_cal_params)

# if total_cal_params["spec_params"]["error_present"]:
#     raise BaseException(total_cal_params["spec_params"]["error_msg"])

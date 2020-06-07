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
        "slot_open": 4.5,
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
        "rate_J": 6,
        "slot_fill_factor": 0.43,
    },
    "calculation": {
        "est_rotor_OD": None,
        "est_stator_OD": None,
        "mag_thick": None,
        "teeth_width": None,
        "york_width": None,
        "slot_height": None,
        "slot_width_front": None,
        "slot_width_back": None,
        "para_conductor": None,
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


def expend_stator_slot(total_cal_params):
    cal_parms = total_cal_params["motor_cal_parms"]
    stator = cal_parms["stator"]

    stator_OD_limit = stator["OD_limit"]
    conductor_OD = cal_parms["coil"]["conductor_OD"]
    membrane_ratio = cal_parms["coil"]["membrane_ratio"]
    coil_turns = cal_parms["calculation"]["coil_turns"]
    slot = cal_parms["stator"]["slot"]
    teeth_width = cal_parms["calculation"]["teeth_width"]
    york_width = cal_parms["calculation"]["york_width"]
    rotor_OD = cal_parms["calculation"]["est_rotor_OD"]
    airgap = cal_parms["airgap"]
    shoes_height_front = cal_parms["stator"]["shoes_height_front"]
    shoes_height_back = cal_parms["stator"]["shoes_height_back"]

    para_conductor = math.ceil(
        total_cal_params["spec_params"]["current_rms"] /
        (cal_parms["coil"]["rate_J"] * (conductor_OD ** 2 * math.pi / 4) * cal_parms["coil"]["Y_para"]))

    coil_area = round(2 * coil_turns * ((conductor_OD *
                                         membrane_ratio) ** 2 * math.pi / 4) * para_conductor, 2)

    est_slot_area = round(coil_area / cal_parms["coil"]["slot_fill_factor"], 2)

    max_slot_height = stator_OD_limit/2 - york_width - \
        shoes_height_front - shoes_height_back - (rotor_OD + airgap*2)/2

    slot_height = york_width  # for slot height & york 1:1

    while slot_height < max_slot_height:
        slot_width_front = (((rotor_OD + airgap*2) + (shoes_height_front +
                                                      shoes_height_back)*2) * math.pi - slot * teeth_width) / slot

        slot_width_back = (((rotor_OD + airgap*2) + (shoes_height_front +
                                                     shoes_height_back + slot_height)*2) * math.pi - slot * teeth_width) / slot

        real_slot_area = (slot_width_front + slot_width_back) / 2 * slot_height + \
            (stator["slot_open"] + slot_width_front) / 2 * shoes_height_back + \
            slot_width_back * stator["slot_corner_arc"]

        if abs((real_slot_area - est_slot_area) / est_slot_area) < 0.01:
            break
        else:
            slot_height += 0.01


    cal_parms["calculation"]["para_conductor"] = para_conductor
    cal_parms["calculation"]["est_stator_OD"] = (round(slot_height, 2) +  york_width + shoes_height_front + shoes_height_back + airgap)*2 + rotor_OD
    cal_parms["calculation"]["slot_height"] = round(slot_height, 2)
    cal_parms["calculation"]["slot_width_front"] = slot_width_front
    cal_parms["calculation"]["slot_width_back"] = slot_width_back

    return total_cal_params


def mech_cal(total_cal_params):
    ktke_validate(total_cal_params) and \
        expend_NBLR(total_cal_params) and \
        expend_stator_teeth_york(total_cal_params) and \
        expend_stator_slot(total_cal_params)

    if total_cal_params["spec_params"]["error_present"]:
        raise BaseException(total_cal_params["spec_params"]["error_msg"])

# import ipdb; ipdb.set_trace()
# ktke_validate(total_cal_params)

# if total_cal_params["spec_params"]["error_present"]:
#     raise BaseException(total_cal_params["spec_params"]["error_msg"])

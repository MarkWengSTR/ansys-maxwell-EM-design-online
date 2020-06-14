from params.ktke_calculation import mech_stucture_cal

def stator_params_assign(total_cal_params):
    stator_params = total_cal_params["stator_params"]
    cal_params = total_cal_params["motor_cal_params"]

    stator_params["Dso"] = str(
        cal_params["calculation"]["est_stator_OD"]) + "mm"
    stator_params["Dsi"] = str(
        cal_params["calculation"]["est_rotor_OD"] + cal_params["airgap"]*2) + "mm"
    stator_params["slot"] = str(cal_params["stator"]["slot"])
    stator_params["Hs0"] = str(
        cal_params["stator"]["shoes_height_front"]) + "mm"
    stator_params["Hs1"] = str(
        cal_params["stator"]["shoes_height_back"]) + "mm"
    stator_params["Bs0"] = str(cal_params["stator"]["slot_open"]) + "mm"
    stator_params["Rs"] = str(cal_params["stator"]["slot_corner_arc"]) + "mm"
    stator_params["Wt"] = str(cal_params["calculation"]["teeth_width"]) + "mm"
    stator_params["Wy"] = str(cal_params["calculation"]["york_width"]) + "mm"

    return total_cal_params


def rotor_params_assign(total_cal_params):
    rotor_params = total_cal_params["rotor_params"]
    cal_params = total_cal_params["motor_cal_params"]

    rotor_params["airgap"] = str(cal_params["airgap"]) + "mm"
    rotor_params["pole"] = str(cal_params["rotor"]["pole"])
    rotor_params["mag_emb"] = str(cal_params["rotor"]["mag_emb"])
    rotor_params["mag_thick"] = str(
        cal_params["calculation"]["mag_thick"]) + "mm"

    return total_cal_params


def other_motor_params_assign(total_cal_params):
    other_motor_params = total_cal_params["other_motor_params"]
    cal_params = total_cal_params["motor_cal_params"]

    other_motor_params["speed_rpm"] = str(cal_params["corner_speed_rpm"]) + "rpm"
    other_motor_params["length"] = str(cal_params["length"]) + "mm"

    return total_cal_params

def excitation_params_assign(total_cal_params):
    excitation_params = total_cal_params["excitation_params"]
    cal_params = total_cal_params["motor_cal_params"]

    excitation_params["N"] = str(cal_params["calculation"]["coil_turns"])
    excitation_params["Im"] = str(cal_params["max_current_rms"]) + "A"

    return total_cal_params

def optiparametric_params_assign(total_cal_params):
    optiparametric_params = total_cal_params["optiparametric_params"]
    cal_params = total_cal_params["motor_cal_params"]

    optiparametric_params["max_power"] = [str(cal_params["max_current_rms"]) + "A", str(cal_params["corner_speed_rpm"]) + "rpm"]
    optiparametric_params["max_speed"] = ["0A", str(cal_params["max_speed_rpm"]) + "rpm"]

    return total_cal_params


# import ipdb; ipdb.set_trace()
def total_params_calculate(ctx):
    total_cal_params = ctx["params"]

    mech_stucture_cal(total_cal_params) and \
        stator_params_assign(total_cal_params) and \
        other_motor_params_assign(total_cal_params) and \
        excitation_params_assign(total_cal_params) and \
        optiparametric_params_assign(total_cal_params) and \
        rotor_params_assign(total_cal_params)

    ctx["params"] = total_cal_params

    return ctx

# total_params_calculate()
# import ipdb; ipdb.set_trace()

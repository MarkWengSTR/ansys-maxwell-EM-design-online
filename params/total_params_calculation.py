from params.ktke_calculation import mech_stucture_cal
from params.spec import spec_params, motor_cal_params
from params.mechanical import stator_params, rotor_params
from params.motor import motor_params
from params.excitation import excitation_params
from params.band import band_params
from params.name import name_params
from params.analysis import analysis_params
from params.optiparametric import optiparametric_variables
from params.report import report_list

total_cal_params = {"spec_params": spec_params,
                    "motor_cal_params": motor_cal_params,
                    "stator_params": stator_params,
                    "rotor_params": rotor_params,
                    "motor_params": motor_params,
                    "excitation_params": excitation_params,
                    "band_params": band_params,
                    "name_params": name_params,
                    "analysis_params": analysis_params,
                    "optiparametric": optiparametric_variables,
                    "report": report_list,
                    }


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


def total_params_calculate():
    mech_stucture_cal(total_cal_params) and \
        stator_params_assign(total_cal_params) and \
        rotor_params_assign(total_cal_params)

    return total_cal_params

# total_params_calculate()
# import ipdb; ipdb.set_trace()

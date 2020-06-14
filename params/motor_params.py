motor_cal_params = {
    "stator": {
        "OD_limit": None,
        "slot": 12,
        "shoes_height_front": 1,
        "shoes_height_back": 1,
        "slot_open": 4.5,
        "slot_corner_arc": 0.5,
    },
    "rotor": {
        "pole": 10,
        "mag_emb": 0.8,  # easier magetization
    },
    "coil": {
        "conductor_OD": 1,
        "y_para": 1,
        "membrane_ratio": 1.075,
        "slot_fill_factor": 0.43,
    },
    "estimate": {
        "kt_ke_ratio":      0.9,
        "max_J": 18,
        "voltage_buffer": 0.9,
        "torque_density":   25,
        "teeth_mag_ang_ratio": 0.6,
        "york_teeth_ratio": 0.7,
        "rotor_OD_ratio": 0.6,
        "bg": 1.2,
        "mag_pc": 7.5,  # for not easy to broke
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
        "real_slot_fill_factor": None,
    },
    "material": {
        "stator": "\"35CS250_20190702\"",
        "rotor": "\"35CS250_20190702\"",
        "magnet": "\"ZH_N44SH_20deg_20190702\"",
        "coil": "\"copper\"",
    },
    "setting": {
        "cycle": 1,
        "split_step": 50
    },
    "voltage_dc": None,
    "length": None,
    "airgap": 0.5,
    "w_factor_10p12s": 0.933,
    "ke":               None,
    "kt":               None,
    "corner_speed_rpm": None,
    "max_speed_rpm":    None,
    "max_current_rms":  None,
}


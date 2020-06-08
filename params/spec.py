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

motor_cal_params = {
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
    },
    "length": 50,
    "airgap": 0.5,
    "w_factor_10p12s": 0.933,
    "estimate": {
        "teeth_mag_ang_ratio": 0.6,
        "york_teeth_ratio": 0.7,
        "rotor_OD_ratio": 0.6,
        "Bg": 1.2,
        "mag_pc": 7.5,  # for not easy to broke
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


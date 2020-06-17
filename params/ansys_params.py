stator_params = {
    "Dsi": "63mm",
    "Dso": "100mm",
    "slot": "12",
    "Hs0": "1mm",
    "Hs1": "1mm",
    "Bs0": "4.5mm",
    "Rs" : "0.5mm",
    "Wt" : "10mm",
    "Wy" : "7mm",
    "Hs2": "Dso/2-Wy-Hs1-Hs0-Dsi/2",
    "Bs1": "((Dsi + (Hs0 + Hs1)*2) *pi -12*Wt)/12",
    "Bs2": "((Dsi + (Hs0 + Hs1 + Hs2)*2) *pi -12*Wt)/12",
    "slot_area": "((Bs1+Bs2)/1mm)/2*(Hs2/1mm)+((Bs0+Bs1)/1mm)/2*(Hs1/1mm)+(Bs2/1mm)*(Rs/1mm)",
}

rotor_params = {
    "airgap": "0.5mm",
    "Dro": "Dsi - airgap*2",
    "Dri": "Dro * 0.4",
    "pole": "10",
    "rotor_type": "1",
    "mag_emb": "0.8",
    "mag_thick": "3mm",
    "mag_width": "0mm",
    "rotor_bridge": "0mm",
    "rotor_rib": "0mm",
}
other_motor_params = {
    "ini_angle": "45.5deg",
    "speed_rpm": None,
    "length": None,
    "multiplier": "1"
}

excitation_params = {
    "N": "5",
    "Im": "0A",
    "f_ele": "speed_rpm/60*(pole/2)/1rpm",
    "lead_ang": "0",
    "I_ph_A": "Im*sqrt(2)*sin((360*f_ele*Time+lead_ang)*pi/180)",
    "I_ph_B": "Im*sqrt(2)*sin((360*f_ele*Time+lead_ang-120)*pi/180)",
    "I_ph_C": "Im*sqrt(2)*sin((360*f_ele*Time+lead_ang+120)*pi/180)",
}

band_params = {
    "rota_band_D": "(Dsi + Dro) / 2",
    "outer_band_D":  "(Dso)*1.1",
    "shaft":       "Dri",
}

name_params = {
    "band": {
        "rotaband": "rotaband",
        "outerband": "outerband",
    },
    "excitation": {
        "conductor_number": "N",
        "phase_I_A": "I_ph_A",
        "phase_I_B": "I_ph_B",
        "phase_I_C": "I_ph_C",
    }
}

analysis_params = {
    "name": "setup1",
    "stoptime": "1/f_ele",
    "timestep": "1/f_ele/50"
}

# dirc cannot apply same key with different value
optiparametric_params = {
    "max_power": ["20A", "3000rpm"],
    "max_speed": ["0A", "3000rpm"],
}

report_list = {
    "torque": ["Moving1.Torque", "Time"],
    "voltage_ph": ["InducedVoltage(Winding_A)", "Time"],
    "voltage_line": ["InducedVoltage(Winding_A)-InducedVoltage(Winding_B)", "Time"],
    "coreloss": ["CoreLoss", "Time"],
}


excitation_params = {
    "N": "5",
    "Im": "0A",
    "f_ele": "speed_rpm/60*(pole/2)/1rpm",
    "lead_ang": "0deg",
    "I_ph_A": "Im*sqrt(2)*sin((360*f_ele*Time+lead_ang)*pi/180)",
    "I_ph_B": "Im*sqrt(2)*sin((360*f_ele*Time+lead_ang-120)*pi/180)",
    "I_ph_C": "Im*sqrt(2)*sin((360*f_ele*Time+lead_ang+120)*pi/180)",
}


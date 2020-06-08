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
    "Dri": "30mm",
    "pole": "10",
    "rotor_type": "1",
    "mag_emb": "0.8",
    "mag_thick": "3mm",
    "mag_width": "0mm",
    "rotor_bridge": "0mm",
    "rotor_rib": "0mm",
}

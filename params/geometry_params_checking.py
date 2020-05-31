from utils.toolsbox  import str_extract_float
from ramda     import *
# import ipdb # ipdb.set_trace()

def geometry_params_checking(params_dir):
    print('Geometry params checking')

    first_large_check_params = [
        ["Dso", "Dsi"],
        ["Dso", "Dro"],
        ["Dsi", "Dro"],
        ["Dsi", "Dri"],
        ["Dro", "Dri"],
    ]

    for params_key1, params_key2 in first_large_check_params:
        if str_extract_float(params_dir[params_key1]) < str_extract_float(params_dir[params_key2]):
            return {'error_present?': True, 'error_msg': f"{params_key1} not support to small than {params_key2}"}

    if filter(lambda v: str_extract_float(v) < 0, params_dir.values()):
       return {'error_present?': True, 'error_msg': "Negtive geomtry parameter"}
    elif str_extract_float(params_dir['slot']) != 18:
       return {'error_present?': True, 'error_msg': f"slot not 18"}
    elif str_extract_float(params_dir['pole']) != 20:
       return {'error_present?': True, 'error_msg': f"pole not 20"}
    elif str_extract_float(params_dir['rotor_type']) != 1:
       return {'error_present?': True, 'error_msg': f"rotor type not spm"}
    elif str_extract_float(params_dir['mag_emb']) > 1:
       return {'error_present?': True, 'error_msg': f"rotor emb large than 1"}

    # notthings happen
    return {'error_present?': False, 'error_msg': 'none'}

# params example
# stator_params = {
# 	"Dsi": "49.1mm",
# 	"Dso": "69mm",
# 	"slot": "18",
# 	"Hs0": "0.35mm",
# 	"Hs1": "0.2mm",
# 	"Hs2": "7.25mm",
# 	"Bs0": "4.5mm",
# 	"Bs1": "6.58mm",
# 	"Bs2": "9.11mm",
# 	"Rs": "0.5mm"
# 	}

# rotor_params = {
# 	"Dro": "48.3mm",
# 	"Dri": "42mm",
# 	"pole": "20",
#         "rotor_type": "1",
# 	"mag_emb": "0.9",
# 	"mag_thick": "1.45mm",
# 	"mag_width": "0mm",
# 	"rotor_bridge": "0mm",
# 	"rotor_rib": "0mm",
# 	}

# print(geometry_params_checking({**stator_params, **rotor_params}))


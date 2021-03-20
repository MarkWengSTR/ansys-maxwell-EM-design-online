import re
import statistics

def str_extract_float(st):
    # "123.45mm" -> 123.45
    return float(re.findall(r"[-+]?\d*\.\d+|\d+", st)[0])
    # return float(re.findall(r"[+-]?\d+(?:\.\d+)?", st)[0])

def avg_leng(*leng_array):
    # ["100mm", "50mm"] = "75mm"
    leng_array = [re.findall(r"[-+]?\d*\.\d+|\d+", i)[0] for i in leng_array]
    leng_float_array = [float(i) for i in leng_array]
    return str(statistics.mean(leng_float_array)) + 'mm'

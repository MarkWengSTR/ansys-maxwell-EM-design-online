import pandas as pd
import os

def result_process(ctx):
    result_ctx = {
        "data_path": ctx["data"]["export_path"],
    }

    return ctx

def process_toruqe():
    tq_df = pd.read_csv(os.path.join(os.getcwd(), "tmp", "2020_06_19_1592578043", "torque.csv"))
    import ipdb; ipdb.set_trace()

process_toruqe()


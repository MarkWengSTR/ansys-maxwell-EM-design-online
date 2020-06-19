import pandas as pd
import os

def output(ctx):
    output_ctx = {
        "data_path": ctx["data"]["export_path"],
    }


    return ctx

def process_toruqe():
    # import ipdb; ipdb.set_trace()
    tq_df = pd.read_csv(os.path.join(os.getcwd(), "tmp", "2020_06_17_1592404192", "torque.csv"))

process_toruqe()


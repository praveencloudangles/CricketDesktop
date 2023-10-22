print("data loading..")

import pandas as pd
import numpy as np

def data_loading():
    missing_values = ["N/a", "na", "Nan", np.nan]
    df = pd.read_csv("ODI_Match_info.csv", na_values=missing_values)

    return df
data_loading()
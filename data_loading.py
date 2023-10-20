print("data loading..")

import pandas as pd
import numpy as np

missing_values = ["N/a", "na", "Nan", np.nan]
df = pd.read_csv("ODI_Match_info.csv", na_values=missing_values)
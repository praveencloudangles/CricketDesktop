print("data analysis..")
from data_loading import data_loading
import numpy as np
def data_analysis():

    data=data_loading()
    print(data.isnull().sum())
    # print("checking null values--------------", data_null)
    print(data.duplicated().sum())
    #print("checking duplicate values------------",data_duplicate)
    print(data.describe())
    # print("checking for outliers-----------------", data_outliers)
    print(data.info())

    for col in data.columns:
        print(col, data[col].nunique())

    return data
data_analysis()

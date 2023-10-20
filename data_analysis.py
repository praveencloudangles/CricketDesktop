print("data analysis..")
from data_loading import df
import numpy as np

data = df

#checking for null values.
data_null = data.isnull().sum()
# print("checking null values--------------", data_null)

data_duplicate = data.duplicated().sum()
# print("checking duplicate values------------",data_duplicate)

data_outliers = data.describe()
# print("checking for outliers-----------------", data_outliers)

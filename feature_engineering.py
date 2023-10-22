from sklearn.calibration import LabelEncoder
from data_cleaning import data_cleaning

def feature_engineering():
    data = data_cleaning()
    label_encoder = LabelEncoder()

    # Checking the datatype for a column
    column_types = data.dtypes
    print(column_types)

    columns_to_encode = ['city', 'toss_decision', 'player_of_match']
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    data.to_csv("cricket_dataset.csv", index=False)

    return data

feature_engineering()
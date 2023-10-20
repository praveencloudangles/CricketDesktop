print("preparing the datset..")
from feature_engineering import final_df

final_df.to_csv('cricket_prediction.csv', index=False)
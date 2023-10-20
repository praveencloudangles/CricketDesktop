print("feature engineering..")
from datavisualization import df
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns 

def feature_engineering():
    label_encoder = LabelEncoder()
    df_copy = df.copy()
    columns_to_encode = ['city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'dl_applied', 'winner', 'win_by_runs', 'win_by_wickets', 'player_of_match']
    for col in columns_to_encode:
        df_copy[col] = label_encoder.fit_transform(df_copy[col])
    final_df=df_copy
    return final_df

feature_engineering()


# # Correlation Matrix.......................
# corrolation = final_df.corr()
# plt.subplots(figsize=(10, 10))
# sns.heatmap(corrolation, cmap='RdBu', annot = True, fmt=".2f", vmin=-1, vmax=1)
# plt.xticks(range(len(corrolation.columns)), corrolation.columns)
# plt.yticks(range(len(corrolation.columns)), corrolation.columns)
# plt.show()
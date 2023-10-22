print("data visualization.....")
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
# from data_cleaning import data_cleaning
from feature_engineering import feature_engineering

def data_visualization():
    data=feature_engineering()
    categ = []
    numer = []

    for col in data.columns:
        if data[col].dtypes == object:
            categ.append(col)
        else:
            numer.append(col)


    print("categorical values-------------", categ)
    print("numercial values---------------", numer)

    for x in numer:
        q75,q25 = np.percentile(data.loc[:,x],[75,25])
        intr_qr = q75-q25    
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)    
        data.loc[data[x] < min,x] = np.nan
        data.loc[data[x] > max,x] = np.nan

    selected_columns = data[["team1", "team2", "toss_winner", 'winner' ,'win_by_runs', 'win_by_wickets']]

    for num in selected_columns:
        plt.figure(figsize=(5,5))
        sns.boxplot(data=selected_columns, x=num)
        plt.xlabel(num)
    plt.show()

    for num in selected_columns:
        plt.figure(figsize=(5, 5))
        sns.violinplot(data=selected_columns, x=num)
        plt.xlabel(num)
    plt.show()

    corr_matrix = data[['city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'win_by_runs', 'win_by_wickets', 'player_of_match']]
    plt.figure(figsize=(10,8))
    sns.heatmap(corr_matrix.corr(), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
    plt.show()

    return data

data_visualization()
print("data cleaning..")
from matplotlib import pyplot as plt
import pandas as pd
from data_analysis import df

data = df

data=data.drop_duplicates()

data = data.dropna()



column_data = {
    'Afghanistan': 0,
    'Africa XI': 1,
    'Asia XI': 2,
    'Australia': 3, 
    'Bangladesh': 4, 
    'Bermuda': 5, 
    'Canada': 6, 
    'England': 7, 
    'Hong Kong': 8, 
    'India': 9, 
    'Ireland': 10,
    'ICC World XI': 11,
    'Jersey': 12, 
    'Kenya': 13, 
    'Namibia': 14, 
    'Nepal': 15, 
    'Netherlands': 16, 
    'New Zealand': 17, 
    'Oman': 18, 
    'Pakistan': 19, 
    'Papua New Guinea': 20, 
    'Scotland': 21, 
    'South Africa': 22, 
    'Sri Lanka': 23, 
    'United Arab Emirates': 24,
    'United States of America': 25,
    'West Indies': 26, 
    'Zimbabwe': 27,
    }


data[['team1', 'team2', 'toss_winner', 'winner']] = data[['team1', 'team2', 'toss_winner', 'winner']].replace(column_data)

# X = data.drop(['winner'], axis=1)
# y = data["winner"]

# y.value_counts()

# y.value_counts().plot.pie(autopct='%.2f')

# plt.show()

# drop_col = ['id', 'season', 'date', 'result', 'umpire1', 'umpire2', 'umpire3', 'venue']

drop_col = ['id', 'result', 'season', 'date', 'venue', 'umpire1', 'umpire2', 'umpire3']
data.drop(columns=drop_col, inplace=True)
# data.to_csv('final_csv.csv', index=False)

df = data
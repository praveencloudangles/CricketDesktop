print("data visualization..")
from data_cleaning import df
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from feature_engineering import feature_engineering

import warnings
warnings.filterwarnings("ignore")

data_vis = df


categ = []
numer = []

for col in data_vis.columns:
    if data_vis[col].dtypes == object:
        categ.append(col)
    else:
        numer.append(col)

print("categorical values----",categ)
print("numerical values----",numer)

for x in numer:
        q75,q25 = np.percentile(data_vis.loc[:,x],[75,25])
        intr_qr = q75-q25    
        max = q75+(1.5*intr_qr)
        min = q25-(1.5*intr_qr)    
        data_vis.loc[data_vis[x] < min,x] = np.nan
        data_vis.loc[data_vis[x] > max,x] = np.nan

for num in numer:
    plt.figure(figsize=(5,5))
    sns.boxplot(data=data_vis, x=num)
    plt.xlabel(num)
plt.show()

# columns_to_plot = ['team1', 'team2', 'toss_winner', 'winner', 'win_by_runs', 'win_by_wickets']

# for column in columns_to_plot:
#     plt.figure(figsize=(5, 5))
#     sns.boxplot(data=data_vis, x=column)
#     plt.xlabel(column)
#     plt.show()
#----------------------------------------------------------------------------------------------------------
# plt.figure(figsize=(5, 5))
# sns.violinplot(data=data_vis, x='team1')
# plt.xlabel('team1')
# plt.show()

# plt.figure(figsize=(5, 5))
# sns.violinplot(data=data_vis, x='team2')
# plt.xlabel('team2')
# plt.show()

# plt.figure(figsize=(5, 5))
# sns.violinplot(data=data_vis, x='toss_winner')
# plt.xlabel('toss_winner')
# plt.show()

# plt.figure(figsize=(5, 5))
# sns.violinplot(data=data_vis, x='winner')
# plt.xlabel('winner')
# plt.show()

# plt.figure(figsize=(5, 5))
# sns.violinplot(data=data_vis, x='win_by_runs')
# plt.xlabel('win_by_runs')
# plt.show()

# plt.figure(figsize=(5, 5))
# sns.violinplot(data=data_vis, x='win_by_wickets')
# plt.xlabel('win_by_wickets')
# plt.show()

# for column in columns_to_plot:
#     plt.figure(figsize=(5, 5))
#     sns.violinplot(data=data_vis, x=column)
#     plt.xlabel(column)
#     plt.show()

for num in numer:
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=data_vis, x=num)
    plt.xlabel(num)
plt.show()

# Assuming 'your_column_name' is the column you want to plot
data = data_vis['toss_winner']

# Count the unique values in the selected column
value_counts = data.value_counts()

# Create a pie chart
plt.figure(figsize=(5, 5))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
plt.title('Pie Chart for toss_winner')
plt.show()

# Correlation Matrix.......................
dataset = feature_engineering()
plt.figure(figsize=(10,8))
sns.heatmap(dataset.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.show()

df =data_vis
# pip install bar-chart-race 
# conda install -c conda-forge bar_chart_race
import pandas as pd 
import matplotlib.pylab as plt
import numpy as np

df = pd.read_csv('./Data/data.csv', sep='\t', engine="python")
# make score columns
# when 1 rank points 100 score 100 rank application points 0 score
df["score"] = 101- df["rank"]

# data cleaning
df["yearID"] = df["yearID"].str.replace("Y","").astype(int)
df["num"] = df["yearID"] * df['weekIndex']
df["num"] = df["yearID"] * df['weekIndex']

# Dataframe making
data = pd.DataFrame(index= list(df["appID"].unique())).reset_index().rename(columns={"index": "appID"})

for i in range(int(len(df)/100)):
    df1 = df.iloc[i*100: (i+1)*100]
    data = pd.merge(data, df1, on="appID", how="outer").fillna(0)

# Data cleaning2 for animation
data = data.drop_duplicates("appID")
data = data.T
data = data.rename(columns = data.iloc[0])
data = data.drop(data.index[0])
data = data.reset_index(drop=True).astype(int)
data.index = (data.index +1).map(str) + "week"

import bar_chart_race as bcr
bcr.bar_chart_race(df = data, 
                   n_bars = 6, 
                   sort='desc',
                   title='mobile',
                   filename = 'mobile.mp4')
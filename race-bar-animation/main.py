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

# Data frame making
data = pd.DataFrame(index= list(df["appID"].unique())).reset_index().rename(columns={"index": "appID"})

for i in range(int(len(df)/100)):
    df1 = df.iloc[i*100: (i+1)*100]
    data = pd.merge(data, df1, on="appID", how="outer").fillna(0)

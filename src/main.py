import pandas as pd


victims = pd.read_csv("./data/2001.csv")

print(victims[victims["Country"].isna()])

print(victims.iloc[628, :])

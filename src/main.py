import pandas as pd


victims = pd.read_csv("./data/2001.csv")

# 413 firefighters / police

# print(victims[victims["Police"] | victims["Firefighter"]])

subset = []
color = "red"

with open(f"./signageGeneration/{color}.txt", "r") as f:
    subset = f.read().split(",")[:-1]
    f.close()
subset = [int(s) - 1 for s in subset]


bigslice = victims.iloc[subset, :]


print(bigslice[bigslice["Police"] | bigslice["Firefighter"]])

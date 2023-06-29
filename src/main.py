import pandas as pd


victims = pd.read_csv("./data/2001.csv")

print(victims[victims["Police"] & victims["Employer"].isna()])

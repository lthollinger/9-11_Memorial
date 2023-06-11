import pandas as pd


victims = pd.read_csv("./data/2001.csv")


# FDNY = victims.loc[victims.Employer == "FDNY", :]
# FDNY.to_csv("./data/firefighters.csv")
# print(FDNY)


mask = victims.Job.str.contains("police")
mask = mask.fillna(False)

options = ["NYPD", "Federal Bureau of Investigation"]
POLICE = victims.loc[((mask) | (victims["Employer"].isin(options))), :]
print(POLICE)

import pandas as pd

victims = pd.read_csv("./data/testList.csv")
FDNY = pd.read_csv("./data/firefighters.csv")

victims["Firefighter"] = False


# print(victims["Name"])
# print(FDNY["Name"])

victims.loc[
    ([FDNY["Name"].str.contains(name).any() for name in victims["Name"]]), "Firefighter"
] = True

print(victims.iloc[290:300])

print(len(victims.loc[victims["Firefighter"] == True, :]))

victims.to_csv("./data/2001.csv", index=False)

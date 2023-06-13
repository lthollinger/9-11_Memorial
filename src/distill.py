import pandas as pd

"""
2977 victims of the attacks

Gets 2001 1993 csv and strips 1993 survivors from it

"""

allyears = pd.read_csv("./data/20011993.csv")
ninetyThree = pd.read_csv("./data/1993.csv")


# print(allyears["Name"])
# print(ninetyThree["Name"])
mask = [not bool(ninetyThree["Name"].isin([x]).sum()) for x in allyears["Name"]]

# 2001 victims only using boolean mask
twoKone = allyears[mask]
print(f"2001 Victims sheet data: {twoKone.shape}")

twoKone.to_csv("./data/2001.csv", index=False)

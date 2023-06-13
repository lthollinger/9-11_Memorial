import pandas as pd

# 2001 victims only
twoKone = pd.read_csv("./data/2001.csv")
print(f"2001 Victims sheet data: {twoKone.shape}")


# if name is in the secondary list, keep it. if it isn't then it's suspicious ¯\_(ツ)_/¯

# cross reference list to secondary list
secondary = pd.read_csv("./data/secondaryList.csv")
print(f"secondary - Victims sheet data: {secondary.shape}")


def crosscheck(name):
    # check if firstname is in the main list
    # check if last name is in main list
    # if these come back to one result, move to the processed list. This should check which names from the big list are also in the small list, narrowing it possibly...
    pass


# some names turn out false due to middle names not matching, abbreviated middle names, or nicknames
mask = [not crosscheck(name) for name in twoKone["Name"]]

# print(mask)

testout = twoKone[mask]

testout.to_csv("./data/problemCrossRefs.csv", index=False)

print(testout)
# mask = [not bool(twoKone["Name"].isin([x]).sum()) for x in secondary["Name"]]
# mask = [not bool(secondary["Name"].isin([x]).sum()) for x in twoKone["Name"]]
# print(f"mask len: {len(mask)}\n{mask}")

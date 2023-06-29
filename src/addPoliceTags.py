import pandas as pd
from name_splitter import rectifyName

# go through police reference list and add a tag to the people it identifies in the main list
VICTIMS_MAIN = pd.read_csv("./data/2001.csv")
VICTIMS_MAIN["Police"] = False

victims = VICTIMS_MAIN.copy(deep=False)
officers = pd.read_csv("./data/oldData/fullPoliceRef.csv")


victims["Name"] = [name.lower() for name in victims["Name"]]


for i, row in officers.iterrows():
    # find subset of police reference list where names match

    subset = victims.loc[
        (
            (victims["Name"].str.contains(row["Last"]))
            & (victims["Name"].str.contains(row["First"]))
        ),
        :,
    ]

    if len(subset) != 1:
        print(f"\n{row.Name}\n{subset}\n")
        print(
            f"Warning! Discrepancy. Enter an index to determine which person to choose. -1 to skip"
        )
        idx = (int)(input("Index: "))
        if idx != -1:
            subset = subset.iloc[idx, :]
            print(f"\n{row.Name}\n{subset}\n\n")
            print(f"{subset.name}")
            input("This was your selection. Any key to continue")
            nameindex = subset.name
        else:
            print("passed")
            continue
    else:
        nameindex = subset.index[0]

    print(row)
    print(subset)
    print("\n\n\n")

import pandas as pd


pref = pd.read_csv("./data/oldData/fullPoliceRef.csv")
pref = pref.sort_values(by=["Last"]).reset_index()

victims = pd.read_csv("./data/2001.csv")
subset = victims[victims["Police"]].reset_index()

# Name,Age,Place,Town/City,Province/State,Country,Job,Employer,Police,Firefighter


def selIdx(key):
    idx = input(f"0 or 1 to select missing {key} value  ||  -1 to skip")
    return idx


for i, row in subset.iterrows():
    print(f"{i}\n{row}\n{pref.iloc[[i], :]}\n\n\n")  # type: ignore

    if pd.isna(row["Employer"]):
        selIdx("Employer")

    if pd.isna(row["Job"]):
        selIdx("Job")

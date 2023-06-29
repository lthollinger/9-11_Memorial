import pandas as pd

"""
PANYNJ - 37 on 9/11
https://www.panynj.gov/police/en/september-11--2001--fallen-papd.html 
VALID


NYPD - 23 on 9/11
https://www.nyc.gov/site/nypd/about/memorials/9-11-tribute.page
VALID
"""

police_ref = pd.read_csv("./data/oldData/policeReference.csv")
victims = pd.read_csv("./data/2001.csv")


departments = police_ref.Department.unique()
"""
'Federal Bureau of Investigation'
'New York City, New York, F.D.'        
'New York City, NY, P.D.'
'New York State Office of Court Administration'
'NY State Department of Taxation & Finance'
'Port Authority of New York/ New Jersey, P.D.'
'U.S. Fish & Wildlife Service'
'U.S. Secret Service'
"""


def rectifyName(name):
    # Removes tail info (age / parenthesis information)
    # name = name.split(",")[0]
    arr = name.split()

    # removes titles
    removetags = [
        "Chief",
        "Lt.",
        "Capt.",
        # "Jr.",
        "Paramedic",
        # "I",
        # II",
        # "III",
        # "IV",
        # "Jr",
        # "Sr",
    ]
    arr = [c for c in arr if c not in removetags]
    arr = [i.title() for i in arr]
    arr = [c for c in arr if c not in removetags]

    name = " ".join(arr).strip()
    return {"Name": name, "First": arr[0].lower(), "Last": arr[-1].lower()}


# print(police_ref)

names = [rectifyName(name) for name in police_ref["Name"]]

police_ref = police_ref.combine_first(pd.DataFrame(names))

# police_ref.to_csv("./data/fullPoliceRef.csv", index=False)


for i, row in police_ref.iterrows():
    # check last
    subset = victims.loc[victims["Name"].str.contains(row["Last"]), :]

    if len(subset) > 1:
        # print(f'\n\nCheck: {row["Name"]}')
        # print(subset)
        subset = subset.loc[subset["Name"].str.contains(row["First"]), :]
        # print(f"\n{subset}")

        if len(subset) > 1:
            print(f'\n\nCheck: {row["Name"]}')
            print(subset)
    if len(subset) < 1:
        print(f"{i} ERROR: {row['Name']}")


"""
All reviews came back right

i'll be including the 72 men in the thing

"""

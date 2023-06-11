import pandas as pd

"""

README:
The following function and modifications took a secondary list and removed prefixes, suffixes, job titles, and ages to identify firefighters based on name


def rectifyName(name):
    # Removes tail info (age / parenthesis information)
    # name = name.split(",")[0]
    arr = name.split()

    # removes titles
    removetags = [
        "Chief",
        "Lt.",
        "Capt.",
        "Jr.",
        "Paramedic",
        "I",
        "II",
        "III",
        "IV",
        "Jr",
        "Sr",
    ]
    arr = [c for c in arr if c not in removetags]

    name = " ".join(arr).strip()
    return {"Name": name, "First": arr[0], "Last": arr[-1]}


FDNY = pd.read_csv("./data/fdnySecondaryList.csv")

names = pd.DataFrame([rectifyName(name) for name in FDNY["Name"]])

names.to_csv("./data/fdnySecondaryList.csv", index=False)

print(names)


"""
primary = pd.read_csv("./data/firefighters.csv")
secondary = pd.read_csv("./data/fdnySecondaryList.csv")

"""
Checks primary list (has errors in the employer data) against secondary list of only the firefighers' names.
Purpose: identify firefighters missing from the FDNY employer data on the primary list
"""


for i, row in secondary.iterrows():
    # print(f"{i} - Checking: {row.Name}")
    # check last name
    temp = primary[[row.Last in name for name in primary["Name"]]]
    # print(len(temp))

    # narrow down w first if multiple with last
    if len(temp) > 1:
        # print(f"\n\n\n\n{i} - Checking: {row.Name}")
        # print(f"Temp: {temp}")
        final = temp[[row.First in name for name in temp["Name"]]]
        # print(f"Final: {final}")
        if len(final) > 1:
            # print(f"\n\n\n\n{i} - Checking: {row.Name}")
            # print(f"Final: {final}")
            pass
    elif len(temp) < 1:
        print(f"FAILED ON: {row.Name}")


"""
Output:

FAILED ON: Thomas O’Hagan
FAILED ON: William O’Keefe
FAILED ON: Frederick Ill
FAILED ON: Daniel O’Callaghan
FAILED ON: John James Tipping
FAILED ON: David Laforge
FAILED ON: Dennis O’Berg
FAILED ON: Patrick J O’Keefe
FAILED ON: Lincoln Quappe


Interpretation:
Some of these are caused because of same last names, different formatting, and accent marks. I've verified each one and learned that "John James Tipping" was actually missing from the primary list

"""

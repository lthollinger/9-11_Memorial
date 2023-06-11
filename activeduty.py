import pandas as pd

"""
Counting Victims Check off



This is 2977!  \/

   Location  Victims
0       WTC     2606    Correct
1     UA175       60    Correct
2      UA93       40    Correct
3      AA11       87    Correct
4      AA77       59    Correct
5  Pentagon      125    Correct

"""


"""
Professions check


Profession  Number
FDNY    343
NYPD    71



"""


# find victims without a place?


def countVictims(key, value):
    return {
        key: value,
        "Victims": victims[[x == value for x in victims[key]]].count().max(),
    }


victims = pd.read_csv("./data/2001.csv")


options = ["US Army", "US Navy"]
military = victims.loc[victims["Employer"].isin(options), :]


mask = military["Job"].str.contains("civilian").fillna(True)

active_duty = military.loc[~mask, :]
print(active_duty)

active_duty.to_csv("./data/activeduty.csv", index=False)

"""
unique = victims.Place.unique()[:-1]
vals = pd.DataFrame([countVictims(place) for place in unique])
print(vals)
"""

# temp = victims.Place.unique()[-1:]

# placeless = victims[[place == temp for place in victims["Place"]]]

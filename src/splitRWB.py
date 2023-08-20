import pandas as pd

victims = pd.read_csv("./data/2001.csv")

# print(victims)


# [print(f"\n\n{v}\nName:{v.name}") for i, v in victims.head(5).iterrows()]


def appendID(color, id):
    id += 1
    print(f"placing {id} in color {color}")
    with open(f"./signageGeneration/{color}.txt", "a") as f:
        f.write(f"{id},")


def clearTXT(color):
    with open(f"./signageGeneration/{color}.txt", "w") as f:
        f.write(f"")


"""
LOGIC:

if red and white full
then blue
else if firefighter or police
place blue

place red
place white



Placing:
add alphabetital id to an array of the proper name
save the array

"""
slots = {"red": 1256, "white": 1116, "blue": 644}

# reset txts
[clearTXT(key) for key in slots]


# shuffles people around
victims = victims.sample(frac=1)

for i, victim in victims.iterrows():
    print(victim["Name"])

    if slots["red"] == 0 and slots["white"] == 0:
        appendID("blue", victim.name)
        slots["blue"] -= 1
        continue
    elif victim["Firefighter"] or victim["Police"]:
        appendID("blue", victim.name)
        slots["blue"] -= 1
        continue

    if slots["red"] != 0:
        appendID("red", victim.name)
        slots["red"] -= 1
        continue

    elif slots["white"] != 0:
        appendID("white", victim.name)
        slots["white"] -= 1
        continue
    else:
        print("ERROR")
        exit(-1)

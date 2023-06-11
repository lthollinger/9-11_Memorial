import pandas as pd


# cross reference list to secondary list
secondary = pd.read_csv("./data/secondaryList.csv")
print(f"secondary - Victims sheet data: {secondary.shape}")


def has_numbers(inputString):
    return any([char.isdigit() for char in inputString])


def upperFirst(s):
    return s[0].isupper()


def hasPeriod(s):
    return s[-1:] == "."


def cleanName(name):
    arr = name.split()
    # checks if last element has numbers in it
    if has_numbers(arr[-1:][0]):
        arr = arr[:-1]

    while len(arr) > 0:
        # if the last element isnt uppercase, chop it
        if not upperFirst(arr[-1:][0]) or hasPeriod(arr[-1:][0]):
            arr = arr[:-1]
        else:
            break

    arr = [word.strip(", ") for word in arr]

    if len(arr) <= 0:
        return None

    temp = {"First": arr[0], "Last": arr[-1:][0]}
    return temp


# check last name first
# if multple results, check first name
# if inconclusive, check middle name

cleaned = [cleanName(name) for name in secondary["Name"]]
cleaned = [i for i in cleaned if i is not None]

df = pd.DataFrame(cleaned)

print(df)

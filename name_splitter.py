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
        ",",
    ]
    arr = [c for c in arr if c not in removetags]
    arr = [i.title().strip(",") for i in arr]
    arr = [c for c in arr if c not in removetags]

    name = " ".join(arr).strip("")
    return {"Name": name, "First": arr[0].lower(), "Last": arr[-1].lower()}

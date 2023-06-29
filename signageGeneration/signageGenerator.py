import subprocess
import os
import pandas as pd
from nameparser import HumanName
import time
import shutil
import random


def addError(idx):
    idx = str(idx)
    with open("errors.txt", "a") as f:
        f.writelines(["\n", idx])
        f.close()
    return 0


def victimData(row: pd.Series):
    name_info = HumanName(row["Name"])
    origin_info = ", ".join(
        [
            sli
            for sli in (row.loc[["Town/City", "Province/State", "Country"]])
            if pd.notna(sli)
        ]
    )

    employment_data = []
    if pd.notna(row["Job"]):
        employment_data.append(row["Job"].title())
    if pd.notna(row["Employer"]):
        employment_data.append(row["Employer"])
    employment_info = ", ".join(employment_data)

    # employment_info = ", ".join(
    #     [sli.title() for sli in (row.loc[["Job", "Employer"]]) if pd.notna(sli)]
    # )

    placeRef = {
        "WTC": "World Trade Center",
        "UA175": "United Airlines Flight 175",
        "UA93": "United Airlines Flight 93",
        "AA11": "American Airlines Flight 11",
        "AA77": "American Airlines Flight 11",
        "Pentagon": "Pentagon",
    }

    data = {
        "FIRST": f"{name_info['first']}",
        "MIDDLE": f"{name_info['middle']}",
        "LAST": f"{name_info['last']} {''.join(name_info['suffix'])}",
        "AGE": f"Aged {row['Age']}",
        "ORIGIN": origin_info,
        "JOB": employment_info,
        "PLACE": f"{placeRef[row['Place']]}",
    }
    for key in data:
        data[key] = f"{data[key]}".strip()
        data[key] = data[key].replace("&", "\\&")
        if len(data[key]) == 0:
            data[key] = " "

    # print(data)
    return data


def createTEX(data: dict, templatePath, outputPath):
    # get template
    tempTEX = ""
    with open(templatePath, "r") as f:
        tempTEX = f.read()
        f.close()
    # print(tempTEX)

    # change template
    for key in data:
        tempTEX = tempTEX.replace(key, data[key])

    # save output
    # fmt: off
    with open(outputPath, "w", encoding='utf-8') as f:
        f.write(tempTEX)
        f.close()
    # fmt: on


def createSignagePDF(row):
    """
    How this works:

    calls createTEX() to create a "document.tex" file with a given user's data at "docPath"

    calls xelatex from terminal to convert the document.tex to a pdf at signageOutput

    moves and renames the pdf in signageOutput to signageStorage

    end.

    """
    #
    docPath = f"./signageGeneration/signageOutput/{row.name}.tex"
    docPath = f"./signageGeneration/signageOutput/document.tex"
    createTEX(
        victimData(row),
        templatePath="./signageGeneration/template.tex",
        outputPath=docPath,
    )

    output_dir = "./signageGeneration/signageOutput"
    command = f"xelatex -jobname=result -halt-on-error -output-directory={output_dir} {docPath}"

    # print("Starting")
    proc = subprocess.Popen(command)
    proc.communicate()
    # print("Ending")

    # print(f"\n\n\nProcessed pdf for {row['Name']}\n\n\n")

    try:
        os.replace(
            output_dir + "/result.pdf",
            f"./signageGeneration/signageStorage/{row.name}.pdf",
        )
    except:
        exit(-1)
        addError(row.name)


def main():
    """
    TODO
    Implement multiple middle names function
    Smart last names function

    Save file to specific location
    """

    victims = pd.read_csv("./data/2001.csv")

    # errorlines = []
    # with open("errors.txt", "r") as f:
    #     for line in f:
    #         errorlines.append(line[:-1])
    #     f.close()

    # [createSignagePDF(victims.iloc[int(line), :]) for line in errorlines]

    # [createSignagePDF(row) for i, row in victims.iloc[450:455, :].iterrows()]

    rootDir = "./signageGeneration/signageStorage"
    pages = []
    for root, dirs, files in os.walk(rootDir, topdown=False):
        for name in files:
            pages.append(name[:-4])

    pages.sort(key=int)
    # print(pages)
    print(len(pages))
    for i in range(2977):
        print(f"{i}   {pages[i]}")

    # 2955
    # createSignagePDF(victims.iloc[2955, :])


if __name__ == "__main__":
    main()

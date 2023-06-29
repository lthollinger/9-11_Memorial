import subprocess
import os
import pandas as pd
from nameparser import HumanName
import time
import shutil
import random


def victimData(row: pd.Series):
    name_info = HumanName(row["Name"])
    origin_info = ", ".join(
        [
            sli
            for sli in (row.loc[["Town/City", "Province/State", "Country"]])
            if pd.notna(sli)
        ]
    )
    employment_info = ", ".join(
        [sli.title() for sli in (row.loc[["Job", "Employer"]]) if pd.notna(sli)]
    )
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

    os.replace(
        output_dir + "/result.pdf",
        f"./signageGeneration/signageStorage/{row.name}.pdf",
    )


def main():
    """
    TODO
    Implement multiple middle names function
    Smart last names function

    Save file to specific location
    """

    victims = pd.read_csv("./data/2001.csv")

    # divide by zero error FIXED
    # createSignagePDF(victims.iloc[20, :])

    # createSignagePDF(victims.iloc[2090, :])

    # unicode / spanish characters error (remove ~n)
    createSignagePDF(victims.iloc[379, :])

    # [createSignagePDF(row) for i, row in victims.iloc[0:20, :].iterrows()]


if __name__ == "__main__":
    main()

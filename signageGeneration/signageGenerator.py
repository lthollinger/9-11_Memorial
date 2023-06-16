import subprocess
import os
import math
import random
import pandas as pd
from nameparser import HumanName
import time


def victimData(row: pd.Series):
    name_info = HumanName(row["Name"])
    origin_info = ', '.join([sli for sli in (row.loc[['Town/City', 'Province/State', 'Country']]) if pd.notna(sli)])
    placeRef = {
        'WTC': 'World Trade Center',
        'UA175': 'United Airlines Flight 175',
        'UA93': 'United Airlines Flight 93',
        'AA11': 'American Airlines Flight 11',
        'AA77': 'American Airlines Flight 11',
        'Pentagon': 'Pentagon'
    }



    data = {
        "FIRST": f"{name_info['first']}",
        "MIDDLE": f"{name_info['middle']}",
        "LAST": f"{name_info['last']} {''.join(name_info['suffix'])}",
        "AGE": f"Aged {row['Age']}",
        "ORIGIN": origin_info,
        "JOB": f"{row['Job']}".title(),
        "PLACE": f"{placeRef[row['Place']]}",
    }
    for key in data:
        data[key] = f'{data[key]}'.strip()

    #print(data)
    return data



def createTEX(data: dict):
    # get template
    tempTEX = ''
    with open('./signageGeneration/template.tex', 'r') as f:
        tempTEX = f.read()
        f.close()
    #print(tempTEX)

    # change template
    for key in data:
        tempTEX = tempTEX.replace(key, data[key])

    # save output
    # fmt: off
    with open("./signageGeneration/signageOutput/document.tex", "w",) as f:
        f.write(tempTEX)
        f.close()
    # fmt: on

def createSignagePDF(row):
    
    

    # janky asl but it's too late at night for me to look into the PATH and environment when this works
    # cmd = r"C:\Users\lucas\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe output.tex"
    # proc = subprocess.Popen(cmd, shell=True, env=os.environ)
    # proc.communicate()

    output_dir = "signageGeneration/signageOutput"
    command = f"xelatex -jobname=result -output-directory={output_dir} ./signageOutput/document.tex"

    proc = subprocess.Popen(command)
    proc.communicate()

    # DONT WIPE OUTPUT AUX --> causes border to become off centered on next render
    # os.unlink('output.aux')


def main():
    """
    TODO
    Implement multiple middle names function
    Smart last names function

    Save file to specific location
    """

    victims = pd.read_csv("./data/2001.csv")

    

    createTEX(victimData(victims.sample(1).iloc[0, :]))


if __name__ == "__main__":
    main()

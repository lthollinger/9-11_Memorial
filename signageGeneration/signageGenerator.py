import subprocess
import os
import math
import random
import pandas as pd
from nameparser import HumanName
import time


def createSignagePDF(row):
    name_info = HumanName(row["Name"])

    data = {
        "FIRST_NAME": f"{name_info['first']}",
        "MIDDLE_NAME": f"{name_info['middle']}",
        "LAST_NAME": f"{name_info['last']} {' '.join(name_info['suffix'])}",
        "AGE": row["Age"],
        "ORIGIN": f"{row['Town/City']}, {row['Country']}"
        if (len(row["Town/City"]) > 0)
        else f"{row['Country']}",
        "JOB": f"{row['Job']}".title(),
        "PLACE": f"{row['Place']}",
    }
    signage = r"""
            \documentclass{article}
            \usepackage{tikz}
            \usetikzlibrary{calc}

            \usepackage{fontspec}
            \usepackage{xcolor}
            \usepackage{pagecolor}

            \setmainfont{CrimsonText-Regular}
            \pagecolor{white}
            \color{black}

            \begin{document}
            \begin{tikzpicture}[overlay, remember picture]
            \draw[line width=2pt] ($(current page.north west)+(1cm,-1cm)$) rectangle ($(current page.south east)+(-1cm,1cm)$);
            \end{tikzpicture}
            \thispagestyle{empty}
            \begin{center}
            \vspace{1.5cm}
            {\fontsize{100pt}{120pt}\selectfont %(FIRST_NAME)s}\\
            \vspace{1cm}
            {\fontsize{40pt}{48pt}\selectfont %(MIDDLE_NAME)s}\\
            \vspace{1cm}
            {\fontsize{100pt}{120pt}\selectfont %(LAST_NAME)s}\\
            \vspace{2cm}


            {\fontsize{36pt}{43.2pt}\selectfont Aged %(AGE)s}\\
            \vspace{0.25cm}
            {\fontsize{36pt}{43.2pt}\selectfont %(ORIGIN)s}\\
            \vspace{2cm}


            {\fontsize{24pt}{28.8pt}\selectfont %(JOB)s}\\
            \vspace{0.25cm}
            {\fontsize{24pt}{28.8pt}\selectfont %(PLACE)s}
            \end{center}
            \end{document}
            """

    signage = signage % data

    # fmt: off
    with open("./signageGeneration/signageOutput/document.tex", "w",) as f:
        f.write(signage)
        f.close()
    # fmt: on

    # janky asl but it's too late at night for me to look into the PATH and environment when this works
    # cmd = r"C:\Users\lucas\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe output.tex"
    # proc = subprocess.Popen(cmd, shell=True, env=os.environ)
    # proc.communicate()
    time.sleep(0.5)
    output_dir = "signageGeneration/signageOutput"
    command = f"xelatex -jobname=result -output-directory={output_dir} ./signageOutput/document.tex"

    proc = subprocess.Popen(command)
    proc.communicate()

    # DONT WIPE OUTPUT AUX --> causes border to become off centered on next render
    # os.unlink('output.aux')


def displayName(info, name):
    print(name) if name != None else print()
    print(
        f"""
    First: {info['first']}
    Middle: {info['middle']}
    Last: {info['last']}
    Suffix: {info['suffix']}
    Nickname: {info['nickname']}
    \n\n
    """
    )


def main():
    """
    TODO
    Implement multiple middle names function
    Smart last names function

    Save file to specific location
    """

    victims = pd.read_csv("./data/2001.csv")
    createSignagePDF(victims.loc[0, :])


if __name__ == "__main__":
    main()

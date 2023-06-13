import subprocess
import os
import math
import random


def createSignagePDF(row):
    data = {
        "FIRST_NAME": f"Joey{random.randint(0, 200)}",
        "MIDDLE_NAME": "B.",
        "LAST_NAME": "Smith",
        "AGE": "30",
        "ORIGIN": "Denver, Colorado",
        "JOB": "Sommolier",
        "PLACE": "Arlington",
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

    with open(f"output.tex", "w") as f:
        f.write(signage)
        f.close()

    # janky asl but it's too late at night for me to look into the PATH and environment when this works
    cmd = r"C:\Users\lucas\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe output.tex"
    proc = subprocess.Popen(cmd, shell=True, env=os.environ)
    proc.communicate()

    os.unlink("output.log")

    # DONT WIPE OUTPUT AUX --> causes border to become off centered on next render
    # os.unlink('output.aux')


def main():
    """
    TODO
    Implement multiple middle names function
    Smart last names function

    Save file to specific location
    """

    createSignagePDF("test")


if __name__ == "__main__":
    main()

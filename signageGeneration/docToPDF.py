import os
import subprocess

name = "Mark"
output_dir = "signageGeneration/signageOutput"
command = f"xelatex -jobname=result -output-directory={output_dir} ../document.tex"

# gen result
# rename and move result
# clear log file (optional bc it gets overwritten anyways)


proc = subprocess.Popen(command)
proc.communicate()

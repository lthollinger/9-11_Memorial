# 911Memorial
 
This repo roughly details my process in converting a list of ~3000 names into an equal length pdf document with their information.

**Important Parts:**

"data" directory

The data directory contains the csv files that have all of the information about the victims


"signageGeneration" directory

The signageGeneration directory is where the magic happens. signageGenerator.py takes each person, formats their data, then applies their data to a LaTeX template, then converts that template to a pdf.
I'm aware that this isn't perfect, efficient, or intended usage but it was quick to implement and got the job done in a reasonable amount of time. If you have any questions feel free to ask because I hardly remember what I wrote either.

"totalOutput.pdf" pdf

This aptly named pdf is the complete output of the generator. It is a 2977 page long pdf, each page representing a half sheet with dimensions of 5.5x8.5 inches. This is what I used to make the display.

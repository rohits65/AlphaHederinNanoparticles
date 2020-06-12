# SLOW and doesn't work

import os

import numpy as np
import pandas as pd

# Open data file
with open("data/plgananoparticlestextset.txt") as file:
    data = file.readlines()

# Figure out where a section starts and ends
sectionIndices = []

for i in range(0, len(data)):
    for j in range(1, 5):
        # If the first few characters of the line start with a digit and is followed by a '.' or ':' THEN a ' ', add it.
        if data[i][0:j].isdigit() and (data[i][j] == '.' or data[i][j] == ':') and data[i][j+1] == ' ':
            sectionIndices.append(i)
            firstLine = ''
            for i in range(i, len(data)):
                secondLine = data[i]
                if secondLine == '\n' and firstLine == '\n':
                    break
                # end if
                firstLine = secondLine
            # end for
            break
        # end if
    # end for
# end for: O(n) = 5n

# Loop through the sections via sectionIndicices and create an array with all the words in that section
for i in range(1, len(sectionIndices)):
    print(data[sectionIndices[i]:sectionIndices[i+1]])
# end for: O(n) =

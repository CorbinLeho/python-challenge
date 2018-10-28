# Modules
import os
import csv


# Set path for file
csvpath = os.path.join(../../../../Desktop/Resources/PyBank.csv)


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if 
            break

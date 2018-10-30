# Modules
import os
import csv

month = []
profit = []

# Set path for file
Bank_csv = os.path.join("PyBank.csv")


# Open the CSV
with open(Bank_csv, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)

    TotalMonths = len(list(csv_reader))
    TotalProfit = 0
    for months in csv_reader:
        TotalProfit += int(row[1])


    

# Set variable for output file
output_file = os.path.join("PyBankSolved.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Date", "Profit/Losses"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
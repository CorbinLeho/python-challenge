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

    TotalMonths = 0
    TotalProfit = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    def AverageChange(MonthlyChange, TotalMonths):

    for row in csv_reader:
        TotalMonths += 1
        TotalProfit += int(row[1])
        GreatestIncrease = max(GreatestIncrease, MonthlyChange)
        GreatestDecrease = min(GreatestDecrease, abs(MonthlyChange))
        MonthlyChange = int(row + 1 [1]) - int(row[1])
        if abs(MonthlyChange) > abs(MonthlyChange):
            GreatestIncrease = 


    

# Set variable for output file
output_file = os.path.join("PyBankSolved.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Date", "Profit/Losses"])

    # Write in zipped rows
  #  writer.writerows()
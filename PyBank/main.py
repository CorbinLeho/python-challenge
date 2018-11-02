# Modules
import os
import csv

month = []
profit = []

# Set path for file
Bank_csv = ("PyBank.csv")


# Open the CSV
with open(Bank_csv, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)

    TotalMonths = 0
    TotalProfit = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    for row in csv_reader:
        TotalMonths += 1
        TotalProfit += float(row[1])
        MonthlyChange = float(row + 1 [1]) - float(row[1])
        GreatestIncrease = max(GreatestIncrease, MonthlyChange)
        GreatestDecrease = min(GreatestDecrease, abs(MonthlyChange))
        
        if abs(MonthlyChange) > abs(MonthlyChange):
            GreatestIncrease = 
            def AverageChange(MonthlyChange, TotalMonths):
def Analysis():
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: " + str(TotalMonths))
    print("Total: $" + str(TotalProfit))
    print("Average Change: $" + str(AverageChange))
    print("Greatest Increase in Profits: " + str(GreatestIncrease))
    print("Greatest Decrease in Profits: " + str(GreatestDecrease))
Analysis()

# Set variable for output file
output_file = os.path.join("PyBankSolved.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Date", "Profit/Losses"])

    # Write in zipped rows
  #  writer.writerows()
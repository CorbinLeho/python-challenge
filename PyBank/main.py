# Modules
import os
import csv

# Set path for file
Bank_csv = ("PyBank.csv")

# Open the CSV
with open(Bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)

    TotalMonths = 0
    TotalProfit = 0
    MonthlyChange = []
    GreatestIncrease = 0
    GreatestDecrease = 0

    for row in csv_reader:
        TotalMonths += 1
        TotalProfit += int(row[1])
        MonthlyChange.append(int(row + 1[1]) - int(row[1]))

    GreatestIncrease = max(MonthlyChange)
    GreatestDecrease = min(MonthlyChange)
    AverageChange = sum(abs(MonthlyChange)) / TotalMonths

    def Analysis(GreatestIncrease, GreatestDecrease, AverageChange, TotalProfit, TotalMonths)
        print("Financial Analysis")
        print("--------------------------")
        print("Total Months: " + str(TotalMonths))
        print("Total: $" + str(TotalProfit))
        print("Average Change: $" + str(AverageChange))
        print("Greatest Increase in Profits: " + str(GreatestIncrease))
        print("Greatest Decrease in Profits: " + str(GreatestDecrease))

    Analysis()

# Set variable for output file
output_file = os.path.join("PyBankSolved.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerows(Analysis())
    writer.close()
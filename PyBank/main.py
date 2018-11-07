# Modules
import os
import csv

# Set path for file
Bank_csv = ("PyBank.csv")

# Initiate Variables
Months = []
MonthlyChange = []


# Open the CSV
with open(Bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)
    # Append lists
    for row in csv_reader:
        Months.append(row[0])
        MonthlyChange.append(int(row[1]))

GreatestIncrease = MonthlyChange[0]
GreatestDecrease = MonthlyChange[0]
TotalProfit = 0

for Change in range(len(MonthlyChange)):
    if MonthlyChange[Change] >= GreatestIncrease:
        GreatestIncrease = MonthlyChange[Change]
        GreatestMonth = Months[Change]
    elif MonthlyChange[Change] <= GreatestDecrease:
        GreatestDecrease = MonthlyChange[Change]
        LeastMonth = Months[Change]
    TotalProfit += MonthlyChange[Change]

TotalMonths = len(Months)
AverageChange = round(TotalProfit / TotalMonths, 2)

print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(TotalMonths))
print("Total: $" + str(TotalProfit))
print("Average Change: $" + str(AverageChange))
print("Greatest Increase in Profits: " + GreatestMonth + " " + str(GreatestIncrease))
print("Greatest Decrease in Profits: " + LeastMonth + " " + str(GreatestDecrease))

# Set variable for output file
output_file = os.path.join("PyBankSolved.txt")

#  Open the output file
with open(output_file, "w") as f:
    # Write the header row
    f.writelines("Financial Analysis" + '\n')
    f.writelines("--------------------------" + '\n')
    f.writelines("Total Months: " + str(TotalMonths) + '\n')
    f.writelines("Total: $" + str(TotalProfit) + '\n')
    f.writelines("Average Change: $" + str(AverageChange) + '\n')
    f.writelines("Greatest Increase in Profits: " + GreatestMonth + " $" + str(GreatestIncrease) + '\n')
    f.writelines("Greatest Decrease in Profits: " + LeastMonth + " $" + str(GreatestDecrease) + '\n')
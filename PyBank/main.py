# Modules
import os
import csv

# Set path for file
Bank_csv = ("PyBank.csv")

# Initiate Variables
Months = []
MonthlyProfits = []
TotalProfit = 0

# Open the CSV
with open(Bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)
    # Append lists
    for row in csv_reader:
        Months.append(row[0])
        MonthlyProfits.append(int(row[1]))


MonthlyChange = []
TotalProfit = sum(MonthlyProfits)

for i in range(1,len(MonthlyProfits)):
    MonthlyChange.append(MonthlyProfits[i] - MonthlyProfits[i-1])
    AverageChange = sum(MonthlyChange)/len(MonthlyChange)
    GreatestIncrease = max(MonthlyChange)
    GreatestDecrease = min(MonthlyChange)
    GreatestMonth = str(Months[MonthlyChange.index(max(MonthlyChange))])
    LeastMonth = str(Months[MonthlyChange.index(min(MonthlyChange))])

z = round(AverageChange, 2)

TotalMonths = len(Months)

print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(TotalMonths))
print("Total: $" + str(TotalProfit))
print("Average Change: $" + str(z))
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
    f.writelines("Average Change: $" + str(z) + '\n')
    f.writelines("Greatest Increase in Profits: " + GreatestMonth + " $" + str(GreatestIncrease) + '\n')
    f.writelines("Greatest Decrease in Profits: " + LeastMonth + " $" + str(GreatestDecrease) + '\n')
# Modules
import os
import csv

month = []
profit = []

# Set path for file
bank_csv = os.path.join(../../../Desktop/Resources/PyBank.csv)


# Open the CSV
with open(bank_csv, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    TotalMonths = len(csv_reader)

    for months in csv_reader:
      for month in months:
          total = 0
          Total_Profit = sum(month.row(2))
    

# Set variable for output file
output_file = os.path.join("PyBank.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
from pathlib import Path
import csv

# Create a file path to the CSV file
fp = Path.cwd() /'csv_report'/ "CashOnHand.csv"

# Read the CSV file and store the records
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    salesRecords = list(reader)

# Reverse the salesRecords list
salesRecords.reverse()

# Calculate the cumulative sum of cash changes for each day
cumulative_sums = {}
for row in salesRecords:
    day = int(row[0])
    cash_change = float(row[3])
    cumulative_sums[day] = cumulative_sums.get(day, 0) + cash_change

# Find the maximum difference between consecutive days' cumulative sums
max_difference = 0
max_difference_day = 0

for i in range(1, len(salesRecords)):
    current_day = int(salesRecords[i][0])
    previous_day = int(salesRecords[i - 1][0])
    current_total = cumulative_sums[current_day]
    previous_total = cumulative_sums[previous_day]
    difference = current_total - previous_total

    if difference > max_difference:
        max_difference = difference
        max_difference_day = current_day

# Print the results
print("Cash-on-Hand if current day is lower than the previous day:", max_difference)
print("Day:", max_difference_day)
print("Amount:", max_difference)
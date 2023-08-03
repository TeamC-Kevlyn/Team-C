from pathlib import Path
import csv

# Provided code to read data from the CSV file
fp = Path.cwd() /"csv_report"/ "CashOnHand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract the header and data separately
header = data[0]
cash_data = data[1:]

def calculate_increment_and_deficit(cash_data):
    highest_increment_date = None
    highest_increment_amount = 0

    highest_deficit_date = None
    highest_deficit_amount = 0

    all_deficits = []

    previous_cash = None

    for row in cash_data:
        day_str, cash_str = row[0], row[1]
        cash = float(cash_str)
        day = int(day_str)
        
        if previous_cash is not None:
            difference = cash - previous_cash
            
            if difference > 0:
                if difference > highest_increment_amount:
                    highest_increment_amount = difference
                    highest_increment_date = day
            
            elif difference < 0:
                if difference < highest_deficit_amount:
                    highest_deficit_amount = difference
                    highest_deficit_date = day
                all_deficits.append((day, abs(difference)))
        
        previous_cash = cash

    return (
        highest_increment_date,
        highest_increment_amount,
        highest_deficit_date,
        highest_deficit_amount,
        all_deficits
    )

(
    highest_increment_date,
    highest_increment_amount,
    highest_deficit_date,
    highest_deficit_amount,
    all_deficits
) = calculate_increment_and_deficit(cash_data)

print("[HIGHEST CASH INCREMENT] Day :", highest_increment_date, ", AMOUNT :", highest_increment_amount)
print("[HIGHEST CASH DEFICIT] Day :", highest_deficit_date, ", AMOUNT :", highest_deficit_amount)

print("\n[CASH DEFICIT]")
for date, deficits in all_deficits:
    print("Day :", date, ", AMOUNT :", deficits)
from pathlib import Path
import csv

# Provided code to read data from the CSV file
fp = Path.cwd() / "CashOnHand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract the header and data separately
header = data[0]
cash_data = data[1:]

def analyze_cash_data(cash_data):
    is_continuous_increase = True
    previous_cash = None
    highest_increment = 0
    highest_increment_amount = 0
    highest_increment_date = None

    all_deficits = []

    for row in cash_data:
        date_str, cash_str = row[0], row[1]
        cash = float(cash_str)
        if previous_cash is not None:
            increment = cash - previous_cash

            if increment <= 0:
                is_continuous_increase = False

            if is_continuous_increase:
                if increment > 0 and increment > highest_increment_amount:
                    highest_increment_amount = increment
                    highest_increment_date = date_str
            else:
                if increment < 0:
                    all_deficits.append((date_str, increment))

        previous_cash = cash

    if is_continuous_increase:
        return (
            f"[HIGHEST CASH SURPLUS] DAY: {highest_increment_date}, AMOUNT: USD {highest_increment_amount:.1f}\n"
        )
    else:
        deficits_output = ""
        for date, deficit in all_deficits:
            deficits_output += f"[CASH DEFECIT] DAY: {date}, AMOUNT: USD {deficit:.1f}\n"
        return deficits_output

result = analyze_cash_data(cash_data)
print(result)

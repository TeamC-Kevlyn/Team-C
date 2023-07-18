from pathlib import Path
import csv

fp = Path.cwd()/'csv_report'/"Overhead.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 
    Overhead_cost=[] 
    for row in reader:
        Overhead_cost.append([row[0],row[1],row[2],row[3]])   

def calculate_overhead_percentage(Overhead_cost):
    total_amount = 0
    expenses = []
    highest_percentage = 0
    highest_category = ""

    for item in Overhead_cost:
        if item[1] not in expenses:
            expenses.append(item[1])

    for expense in expenses:
        category_amount = 0
        for item in Overhead_cost:
            if item[1] == expense:
                category_amount += int(item[3])
        total_amount += category_amount

    for expense in expenses:
        category_amount = 0
        for item in Overhead_cost:
            if item[1] == expense:
                category_amount += int(item[3])
        percentage = (category_amount / total_amount) * 100

        if percentage > highest_percentage:
            highest_percentage = round(percentage,2)
            highest_category = expense

    return f'[HIGHEST OVERHEAD] {highest_category} : {highest_percentage}%' 
print(calculate_overhead_percentage(Overhead_cost))

from pathlib import Path
import csv

fp = Path.cwd()/'csv_report'/"Overhead.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 
    Overhead_cost=[] 
    for row in reader:
        Overhead_cost.append([row[0],row[1],row[2],row[3]])   

# Category = [] 
# for item in Overhead:
#     if item[1] not in Category: 
#         Category.append(item[1])
# print(Category)

def Overhead():
    """
    Function calculate all overhead categories to find the highest overhead category
    """
    Expenses = [] 
    for item in Overhead_cost:
        if item[1] not in Expenses: 
            Expenses.append(item[1])

    highest_total_amount = 0
    highest_overhead_category = None

    for expense in Expenses:
        total_amount = 0

        for item in Overhead_cost:
            if expense == item[1]:
                total_amount += int(item[3])

        if total_amount > highest_total_amount:
            highest_total_amount = total_amount
            highest_overhead_category = expense
    
        Expenses.append((item[0], item[1], item[2], item[3]))
    return Expenses







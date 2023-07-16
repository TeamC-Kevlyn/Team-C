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
    Function calculates all overhead categories and their percentages of the total amount
    """

    total_amount = sum(int(item[3]))

    Expenses = []
    for item in Overhead_cost:
        if item[1] not in Expenses:
            Expenses.append(item[1])

    percentages = []
    for expense in Expenses:
        category_amount = 0
        for item in Overhead_cost:
            if item[1] == expense:
                category_amount += int(item[3])
        percentage = (category_amount / total_amount) * 100
        percentages[expense] = round(percentage,2)

        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_category = item[0]
    return highest_category
print(Overhead())







from pathlib import Path
import csv


# create a file to csv file.
fp = Path.cwd()/"csv_report"/"profits and loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    data=list(reader)

for item in data:
    item[0]= int(item[0])
    item[1]= int(item[1])
    item[2]= int(item[2])
    item[3]= int(item[3])
    item[4]= int(item[4])
# Calculate the difference in net profit between consecutive days
def calculate_net_profit_difference(data):
    net_profit_difference = []
    for item in range(1, len(data)):
        difference = data[item][4] - data[item - 1][4]
        net_profit_difference.append(difference)
    return net_profit_difference

# Find the day and amount with the highest increment in net profit
def find_highest_increment(data):
    net_profit_difference = calculate_net_profit_difference(data)

    max_increment = max(net_profit_difference)
    max_increment_index = net_profit_difference.index(max_increment) + 1
    max_increment_day = data[max_increment_index][0]
    return max_increment_day, max_increment

increment = find_highest_increment(data)

for item in range(1, len(data)):
    previous_net_profit = data[item - 1][4]
    current_net_profit = data[item][4]
    
    if current_net_profit < previous_net_profit:
        difference = previous_net_profit - current_net_profit
        print(f"[NET PROFIT DEFECIT] Day : {data[item][0]} , AMOUNT : {difference}")

print("Day and Amount of the highest net profit increment:", increment)

def find_highest_deficit(data):
    highest_deficit = 0
    deficit_day = 0
    for item in range(1, len(data)):
        current_day = data[item]
        previous_day = data[item - 1]
        net_profit_current = current_day[4]
        net_profit_previous = previous_day[4]
        
        if net_profit_current < net_profit_previous:
            diff = net_profit_current - net_profit_previous
            if diff < highest_deficit:
                highest_deficit = diff
                deficit_day = current_day[0]
    return deficit_day, highest_deficit

deficit= find_highest_deficit(data)

print("Day and Amount of the highest net profit deficit:", deficit)

# create a file to csv file.
fp = Path.cwd()/'csv_report'/"Overhead.csv"

# read the csv file to append overhead from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    # create an empty list to store days and cost of operating record
    Overhead_cost= []
    #  append days and cost of operating record into the Overhead_cost list
    for row in reader:
        # get the Day, Items, Note, Amount for each record and append the Overhead_cost list
        Overhead_cost.append([row[0],row[1],row[2],row[3]])   

def calculate_overhead_percentage(Overhead_cost):
    expenses = [] # create an empty list
    # initialise variables
    total_amount = 0
    highest_percentage = 0
    highest_category = ""

    # append expenses to expenses list
    for item in Overhead_cost:
        if item[1] not in expenses:
            expenses.append(item[1])

    # calculate the total expense  
    for expense in expenses:
        category_amount = 0
        for item in Overhead_cost:
            if item[1] == expense:
                category_amount += int(item[3])
        total_amount += category_amount

    # calculate expense for each category
    for expense in expenses:
        category_amount = 0
        for item in Overhead_cost:
            if item[1] == expense:
                category_amount += int(item[3])
        # find the percentage of expense for each category
        percentage = (category_amount / total_amount) * 100

        # compare and find the highest percentage and category
        if percentage > highest_percentage:
            highest_percentage = round(percentage,2)
            highest_category = expense

    # return and print the highest overhead + category
    return f'[HIGHEST OVERHEAD] {highest_category} : {highest_percentage}%' 
print(calculate_overhead_percentage(Overhead_cost))

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



with open('summary_report.txt', 'w') as file:
    file.write(calculate_overhead_percentage(Overhead_cost))
    file.write(f"\n[CASH DEFICIT] DAY: {highest_deficit_date} AMOUNT: {highest_deficit_amount}")
    file.write(f"\n[NET PROFIT DEFECIT] {deficit}")
    

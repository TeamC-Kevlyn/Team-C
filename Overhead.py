from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"Overhead.csv"

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

def Overhead():
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

Overhead()

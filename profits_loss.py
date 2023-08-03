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


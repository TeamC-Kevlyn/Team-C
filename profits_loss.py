from pathlib import Path
import csv


# create a file to csv file.
fp = Path.cwd()/"profits and loss.csv"

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

def calculate_net_profit_difference():
    for item in range(1, len(data)):
        previous_net_profit = data[item - 1][4]
        current_net_profit = data[item][4]
        
        if current_net_profit < previous_net_profit:
            difference = previous_net_profit - current_net_profit
            print(f"[NET PROFIT DEFECIT] Day : {data[item][0]} , AMOUNT : {difference}")
        elif current_net_profit > previous_net_profit:
            difference = current_net_profit - previous_net_profit
            print(f"[NET PROFIT SURPLUS] Day : {data[item][0]} , AMOUNT : {difference}")

calculate_net_profit_difference()  


from pathlib import Path
import csv


# create a file to csv file.
fp = Path.cwd()/"profits and loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    data=list(reader)

def profit_loss():
    for item in data:
        item[0]= int(item[0])
        item[1]= float(item[1])
        item[2]= float(item[2])
        item[3]= float(item[3])
        item[4]= float(item[4])

    def calculate_net_profit_deficit_or_highest_increment(data):
        net_profit_difference= []
        for item in range(1,len(data)):
            difference = data[item][4] - data[item - 1][4]
            net_profit_difference.append(difference)


        has_net_profit_deficit = False
        for item in range(1, len(data)):
            previous_net_profit = data[item - 1][4]
            current_net_profit = data[item][4]

            if current_net_profit < previous_net_profit:
                difference = previous_net_profit - current_net_profit
                has_net_profit_deficit = True
                print(f"[NET PROFIT DEFICIT] Day : {data[item][0]}, AMOUNT : {difference}")

        if not has_net_profit_deficit:
            highest_increment_date = None
            highest_increment_amount = 0
            previous_net_profit = 0  # Initialize the previous net profit before the loop

            for row in data:
                day, net_profit = row[0], row[4]
                net_profit = float(net_profit)
                day = int(day)

                difference = net_profit - previous_net_profit  # Calculate the difference between current and previous net profits
                previous_net_profit = net_profit  # Update the previous net profit for the next iteration

                if difference > 0:
                    if difference > highest_increment_amount:
                        highest_increment_amount = difference
                        highest_increment_date = day

            if highest_increment_date is not None:
                print(f"[HIGHEST NET PROFIT SURPLUS] DAY : {highest_increment_date}, AMOUNT : {highest_increment_amount}")

    calculate_net_profit_deficit_or_highest_increment(data)

# profit_loss()


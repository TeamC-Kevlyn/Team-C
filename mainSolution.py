# import csv_report,CashOnHand,Overhead,profits_loss

# def main ():

#     forex = csv_report.api_function()
#     Overhead.overhead_function(forex)
#     CashOnHand.cashonhand_function(forex)
#     profits_loss.profitloss_function(forex)

#     main()

import Overhead

Overhead_result = Overhead.calculate_overhead_percentage()

with open('summary_report.txt', 'w') as file:
    file.write(Overhead_result)
    # file.write(f"\n[CASH DEFICIT] DAY: {highest_deficit_date} AMOUNT: {highest_deficit_amount}")
    # file.write(f"\n[NET PROFIT DEFECIT] {deficit}")

import Overhead, CashOnHand, profits_loss

def main():

    overhead_result = Overhead.calculate_overhead_percentage(Overhead.Overhead_cost)
    cashonhand_results = CashOnHand.analyze_cash_data(CashOnHand.cash_data)
    profitnloss_results = profits_loss.calculate_net_profit_deficit_or_highest_increment(profits_loss.data)
    return f'{overhead_result}\n{cashonhand_results}{profitnloss_results}'


with open('summary_report.txt', 'w') as file:
    file.write(str(main()))


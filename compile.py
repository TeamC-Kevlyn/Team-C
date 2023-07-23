from pathlib import Path
import csv


# create a file to csv file.
fp = Path.cwd()/"profits and loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    data=[]
    for row in reader:
        data.append([row[0],row[1],row[2],row[3],row[4]])
# print(data)    

data= [['1', '0', '0', '12600', '-12600'], ['2', '0', '0', '341580', '-341580'], ['3', '72495', '29184', '370560', '-341376'], ['4', '231526', '93353', '418945', '-325592'], ['5', '418412', '197377', '480680', '-283303'], ['6', '641735', '317953', '530257', '-212304'], ['7', '4372434', '1055412', '572776', '482636'], ['8', '4582070', '1188442', '608903', '579539'], ['9', '4944421', '1329258', '659610', '669648'], ['10', '8321435', '2784837', '691052', '2093785'], ['11', '9488205', '3518054', '723730', '2794324'], ['12', '10391644', '4046675', '792801', '3253874'], ['13', '12554845', '4810105', '830009', '3980096'], ['14', '15426202', '6246567', '908912', '5337655'], ['15', '15620275', '6372898', '981034', '5391864'], ['16', '15819536', '6502550', '1068546', '5434004'], ['17', '18947695', '7429839', '1158160', '6271679'], ['18', '19276560', '7592164', '1194738', '6397426'], ['19', '19477952', '7718691', '1324231', '6394460'], ['20', '19866099', '8009484', '1437236', '6572248'], ['21', '24286397', '8677198', '1491146', '7186052'], ['22', '24711792', '8859060', '1535163', '7323897'], ['23', '24929710', '8993500', '1635211', '7358289'], ['24', '27893394', '9647711', '1706212', '7941499'], ['25', '28109256', '9780729', '1770983', '8009746'], ['26', '29691540', '10064235', '1827480', '8236755'], ['27', '32770468', '10785902', '1898667', '8887235'], ['28', '33261273', '10955542', '1970033', '8985509'], ['29', '34831522', '11300094', '2070600', '9229494'], ['30', '36866193', '11710610', '2155820', '9554790'], ['31', '37098693', '11832973', '2221642', '9611331'], ['32', '39755113', '12218755', '2274309', '9944446'], ['33', '42128820', '12683025', '2347805', '10335220'], ['34', '43663287', '12912362', '2404774', '10507588'], ['35', '45739848', '13077456', '2476468', '10600988'], ['36', '45968013', '13191338', '2552378', '10638960'], ['37', '47215684', '13842304', '2713215', '11129089'], ['38', '48460669', '14560060', '2799340', '11760720'], ['39', '50597031', '15295971', '2933943', '12362028'], ['40', '55573520', '15497820', '3042532', '12455288'], ['41', '55906967', '15403444', '3120199', '12283245'], ['42', '59163655', '15822230', '3195310', '12626920'], ['43', '62042871', '16302093', '3295235', '13006858'], ['44', '64192614', '16743108', '3403985', '13339123'], ['45', '64459623', '16861381', '3515859', '13345522'], ['46', '68962075', '17149520', '3630654', '13518866'], ['47', '71458415', '17426478', '3720485', '13705993'], ['48', '71668077', '17504902', '3810120', '13694782'], ['49', '73085724', '17984867', '3919846', '14065021'], ['50', '74644228', '18287127', '4009562', '14277565'], ['51', '77104044', '18947786', '4094347', '14853439'], ['52', '78584985', '19250055', '4177263', '15072792'], ['53', '78689668', '19318123', '4263633', '15054490'], ['54', '79033541', '19441420', '4498169', '14943251'], ['55', '79816900', '19823481', '4658586', '15164895'], ['56', '83591249', '21961078', '4866647', '17094431'], ['57', '83924920', '22205724', '5026083', '17179641'], ['58', '86098108', '23405747', '5292341', '18113406'], ['59', '86235206', '23500690', '5461468', '18039222'], ['60', '86347716', '23580672', '5585379', '17995293'], ['61', '86507384', '23684832', '5731787', '17953045'], ['62', '86943017', '24086742', '5880722', '18206020'], ['63', '87303521', '24228027', '5988430', '18239597'], ['64', '87885657', '24445847', '6129918', '18315929'], ['65', '88393299', '24852600', '6267022', '18585578'], ['66', '89021955', '25072376', '6394410', '18677966'], ['67', '89193340', '25201671', '6532404', '18669267'], ['68', '90460993', '25605580', '6699759', '18905821'], ['69', '90942056', '25715656', '6819695', '18895961'], ['70', '91422043', '25824602', '6956246', '18868356'], ['71', '91839126', '26198652', '7060979', '19137673'], ['72', '92313596', '26627490', '7212837', '19414653'], ['73', '93852449', '27165709', '7341877', '19823832'], ['74', '94604016', '27354001', '7525199', '19828802'], ['75', '95050642', '27715475', '7684733', '20030742'], ['76', '95275054', '27845729', '7826791', '20018938'], ['77', '96220956', '27644068', '8031702', '19612366'], ['78', '99034123', '27507778', '8198850', '19308928'], ['79', '100201406', '28346849', '8331084', '20015765'], ['80', '102064364', '28640579', '8508466', '20132113'], ['81', '104732001', '28869282', '8653912', '20215370'], ['82', '105764277', '29597950', '8791907', '20806043'], ['83', '105924282', '29702381', '8939447', '20762934'], ['84', '106999477', '29959709', '9098889', '20854320'], ['85', '107153531', '30059866', '9283201', '20755665'], ['86', '107319423', '30166051', '9395318', '20720733'], ['87', '107488170', '30273785', '9506382', '20703903'], ['88', '108477756', '30364916', '9610239', '20686677'], ['89', '108625555', '30458540', '9690968', '20695072'], ['90', '108793952', '30565153', '9773610', '20719043']]

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

# def increment():
increment = find_highest_increment(data)

for item in range(1, len(data)):
    previous_net_profit = data[item - 1][4]
    current_net_profit = data[item][4]
    
    if current_net_profit < previous_net_profit:
        difference = previous_net_profit - current_net_profit
        day = data[item][0]
        print(f"[NET PROFIT DEFECIT] Day : {day} , AMOUNT : {difference}")
    # print("Day and Amount of the highest net profit increment:", increment)
print("Day and Amount of the highest net profit increment:", increment)
# increment()

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

# Create a file path to the CSV file
fp = Path.cwd() / "CashOnHand.csv"

# Read the CSV file and store the records
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    salesRecords = list(reader)

# Reverse the salesRecords list
salesRecords.reverse()

# Calculate the cumulative sum of cash changes for each day
# def cashonhand():
cumulative_sums = {}
for row in salesRecords:
    day = int(row[0])
    cash_change = float(row[3])
    cumulative_sums[day] = cumulative_sums.get(day, 0) + cash_change

# Find the maximum difference between consecutive days' cumulative sums
max_difference = 0
max_difference_day = 0

for i in range(1, len(salesRecords)):
    current_day = int(salesRecords[i][0])
    previous_day = int(salesRecords[i - 1][0])
    current_total = cumulative_sums[current_day]
    previous_total = cumulative_sums[previous_day]
    difference = current_total - previous_total

    if difference > max_difference:
        max_difference = difference
        max_difference_day = current_day

# Print the results
print("Cash-on-Hand if current day is lower than the previous day:", max_difference)
print("Day:", max_difference_day)
print("Amount:", max_difference)

# cashonhand()



with open('summary_report.txt', 'w') as file:
    file.write(calculate_overhead_percentage(Overhead_cost))
    file.write(f"\n[CASH DEFICIT] DAY: {max_difference_day} AMOUNT: {max_difference}")
    file.write(f"\n[NET PROFIT DEFECIT] {increment}")
    

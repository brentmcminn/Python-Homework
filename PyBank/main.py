from pathlib import Path
import csv


csvpath = Path('C:/Users/brent/RU-HOU-FIN-PT-07-2019-U-C/hw/02-Python/Instructions/PyBank/Resources/budget_data.csv')


#over the entire perio
profits = []
months = []
change_profits = []


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    for row in csvreader:
         
            #= prints rows of dates and P/l
         # Set the 'name', 'count', and 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations
        
        
        month = (row[0])
        profit = int(row[1])
        profits.append(profit) 
        months.append(month)
        
        
    for i in range(len(profits)-1):
        change = (profits[i+1] - profits[i])
        change_profits.append(change)
        
     
        

#initialize all variables 



max_profit = 0
min_profit = 0
max_change = 0
min_change = 0
total_change = 0
total_profit = 0
months_count = 0



#this loops through change_profits to see 
#max_change or min_change for change in total_change


#change takes the value of each element in the list change_profits and adds it 
#to total_change which is listed above as a variable

for change in change_profits:
    
    total_change += change
    
    if min_change == 0:
        min_change = change
        max_change = change
    elif change < min_change:
        min_change = change
    elif change > max_change:
        max_change = change
        
        
#this loops profits to find highest 
#and low with total_month count and total profit for profit in profits:


for profit in profits:

    months_count += 1
    total_profit += profit 
    
    if min_profit == 0:
        min_profit = profit
        max_profit = profit
    elif profit < min_profit:
        min_profit = profit
    elif profit > max_profit:
        max_profit = profit
        
        

index_max = (change_profits.index(max_change))+1
index_min = (change_profits.index(min_change))+1       
            
print(f"total months: {months_count}")
print(f"the total profit is: ${total_profit}")
print(f"Average Change: ${int(total_change/months_count)}")
print(f"Greatest Increase in Profits: ${months[index_max]}: ${max_change}")
print(f"Greatest Decrease in Profits:${months[index_min]}: ${min_change}")

#sets path for the output.csv
output = Path("output.txt")


#open the output path as a file and pass into the 'csv.writer()' function

#set the delimiter/separater as a ','

with open(output, 'w') as csvfile:
    csvwriter = csvwriter(csvfile, delimiter = ',')

#loop through the list of records and write everyrecord to the output csv file

    for record in records:
        csvwriter.writerow(record)


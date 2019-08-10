from pathlib import Path
import csv
import numpy as np

csvpath = Path('C:/Users/brent/RU-HOU-FIN-PT-07-2019-U-C/hw/02-Python/Instructions/PyBank/Resources/budget_data.csv')


#over the entire perio
profits = []
months = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    for row in csvreader:       
        month = (row[0])
        profit = int(row[1])
        profits.append(profit) 
        months.append(month)
#print(profits)


#initialize all variables 
max_profit = 0
min_profit = 0
total_profit = 0
months_count = 0
average_change_profit = np.mean(np.diff(profits))


for profit in profits: 
    months_count += 1
    total_profit += profit 
        
    if min_profit == 0:
        min_profit = profit
        max_profit = profit 
    elif min_profit < profit:
        min_profit = profit
    elif max_profit > profit:
        max_profit = profit 
        
        
        
        

index_max = profits.index(max_profit)
index_min = profits.index(min_profit)        
            
print(f"total months: {months_count}")
print(f"the total profit is: ${total_profit}")
print(f"Average Change: ${average_change_profit}")
print(f"Greatest Increase in Profits: ${months[index_max]}{max_profit}")
print(f"Greatest Decrease in Profits:${months[index_min]}{min_profit}")

print(max(np.diff(profits)))
print(min(np.diff(profits)))





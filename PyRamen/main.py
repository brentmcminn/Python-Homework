from pathlib import Path
import csv
import numpy as np

csvpath = Path('C:/Users/brent/RU-HOU-FIN-PT-07-2019-U-C/hw/02-Python/Instructions/PyBank/Resources/menu_data.csv')


#over the entire perio
menu = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    for row in csvreader:       
        month = (row[0])
        profit = int(row[1])
        profits.append(profit) 
        months.append(month)
#print(profits)
import os
import csv

csv_path = 'budget_data.csv'

months = []
profit_loss = []

with open(csv_path,newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(row[1])

#Total Months
print ("Total Months: " + str(len(months)))

#Total
profit_loss = [int(i) for i in profit_loss]
total = sum(profit_loss)
print("Total: " + str(total))

#Average Change



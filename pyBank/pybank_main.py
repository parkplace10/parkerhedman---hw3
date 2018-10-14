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
       

#Financial Analysis
print("""
Financial Analysis
------------------------------------""")


#Total Months
print ("Total Months: " + str(len(months)))

#Total
profit_loss = [int(i) for i in profit_loss]
total = sum(profit_loss)
total_formatted = '${:,.2f}'.format(total)
print("Total: " + str(total_formatted))

#Average Change
profit_change = 0
monthly_change = []
num_months = range(len(months)-1)
for month in num_months:
    monthly_change.append(int(profit_loss[month+1]) - int(profit_loss[month]))

count_months = len(months)-1
average_change = sum(monthly_change) / count_months
average_change_formatted = '${:,.2f}'.format(average_change)
print("Average change: " + str(average_change_formatted))

#Greatest Increase
greatest_increase = 0
greatest_increase_month_index = 0
for month in num_months:
    if monthly_change[month]>greatest_increase:
        greatest_increase = monthly_change[month]
        greatest_increase_month_index = month + 1

greatest_increase_month = months[greatest_increase_month_index]
greatest_increase_formatted = '${:,.2f}'.format(greatest_increase)
print(f"Greatest increase: {greatest_increase_formatted} ({greatest_increase_month})")

#Greatest Decrease
greatest_decrease = 0
greatest_decrease_month_index = 0
for month in num_months:
    if monthly_change[month]<greatest_decrease:
        greatest_decrease = monthly_change[month]
        greatest_decrease_month_index = month + 1

greatest_decrease_month = months[greatest_decrease_month_index]
greatest_decrease_formatted = '${:,.2f}'.format(greatest_decrease)
print(f"Greatest increase: {greatest_decrease_formatted} ({greatest_decrease_month})")

print("------------------------------------")   


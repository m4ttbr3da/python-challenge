# Modules
import os
import csv

# Establish file path to budget_data.csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the budget_data.csv file using CSV module
with open(csvpath) as csv_file:
    budget_data = csv.reader(csv_file, delimiter=',')

# Skip the header row
    next(budget_data)

# Sets a variable for the total number of months included in the dataset
    all_rows = list(budget_data)

# Sets a variable for the net total amount of "Profit/Losses" over the entire period, and sums the "Profit/Loss" column
    total_profit_loss = 0
    for row in all_rows:
        total_profit_loss += float(row[1]) 

# Creates a variable for the average of the changes in "Profit/Losses" over the entire period

    average_monthly_change = total_profit_loss / len(all_rows)
    
# Creates a variable for the greatest increase in profits (date and amount) over the entire period
    greatest_monthly_profit = 0
    most_profitable_month = 0
    for row in all_rows:
        if float(row[1]) > greatest_monthly_profit:
            greatest_monthly_profit = float(row[1])
            most_profitable_month = row[0]

# Creates a variable for the greatest decrease in losses (date and amount) over the entire period
    greatest_monthly_loss = 0
    least_profitable_month = 0
    for row in all_rows:
        if float(row[1]) < greatest_monthly_loss:
            greatest_monthly_loss = float(row[1])
            least_profitable_month = row[0]
    
# Print out financial summary to the terminal
    print(f'FINANCIAL SUMMARY')
    print(f'___________________________')
    print(f'Total Months:  {len(all_rows)}')
    
    if total_profit_loss > 0:
        print('Total Profit: ${:,.2f}'.format(total_profit_loss))
    else:
        print('Total Loss: $({:,.2f})'.format(total_profit_loss))
    
    if average_monthly_change > 0:
        print('Average Monthly Change: +${:,.2f}'.format(average_monthly_change))
    else:
        print('Average Monthly Change: $({:,.2f})'.format(average_monthly_change*-1))
    
    print(f'Greatest Monthly Profit Increase: {most_profitable_month} -> ' + '+${:,.2f}'.format(greatest_monthly_profit))
    
    print(f'Greatest Monthly Loss: {least_profitable_month} -> ' + '$({:,.2f})'.format(greatest_monthly_loss*-1))

# Create a text file with the financial summary
    print(f'FINANCIAL SUMMARY', file=open("financial_summary.txt","w"))
    print(f'___________________________', file=open("financial_summary.txt","a"))
    print(f'Total Months:  {len(all_rows)}', file=open("financial_summary.txt","a"))
    
    if total_profit_loss > 0:
        print('Total Profit: ${:,.2f}'.format(total_profit_loss), file=open("financial_summary.txt","a"))
    else:
        print('Total Loss: $({:,.2f})'.format(total_profit_loss), file=open("financial_summary.txt","a"))
    
    if average_monthly_change > 0:
        print('Average Monthly Change: +${:,.2f}'.format(average_monthly_change), file=open("financial_summary.txt","a"))
    else:
        print('Average Monthly Change: $({:,.2f})'.format(average_monthly_change*-1), file=open("financial_summary.txt","a"))
    
    print(f'Greatest Monthly Profit Increase: {most_profitable_month} -> ' + '+${:,.2f}'.format(greatest_monthly_profit), file=open("financial_summary.txt","a"))
    
    print(f'Greatest Monthly Loss: {least_profitable_month} -> ' + '$({:,.2f})'.format(greatest_monthly_loss*-1), file=open("financial_summary.txt","a"))
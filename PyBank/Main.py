# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:40:55 2020

@author: citiz
"""
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#print(csvpath)

#  open csv file with reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')


    csv_header = next(csvreader)
    counter = 0
    total_PL = 0
    max_date = ''
    max_diff = 0
    prev = 0
    diff = 0
    low_diff = 0
    low_date = ''
    total_diff = 0
    
    
    for row in csvreader:
        counter = counter + 1 #row counter of months
        profit_loss = float(row[1])
        total_PL = total_PL + profit_loss 
    #print(total_PL)
    #print(counter)
    
#The greatest increase in profits (date and amount) over the entire period
        diff = profit_loss - prev 
        prev = profit_loss
        if diff > max_diff:
            max_diff = diff
            max_date = row[0]
    #print(max_diff)
    #print(max_date)
    
#The greatest decrease in losses (date and amount) over the entire period
        if diff < low_diff:
            low_diff = diff
            low_date = row[0]
            
#The average of the changes in "Profit/Losses" over the entire period
        if counter > 1:   #The average of the changes in "Profit/Losses" over the entire period
            total_diff += diff
    #print(low_diff)
    #print(low_date)

#output for text file
    average_diff = round(total_diff/(counter - 1), 2)
    #print(average_diff)


    header = 'Financial Analysis\n'
    divider = '----------------------------\n'
    total = 'Total: $%.0f \n'%total_PL
    ttlMonths = f'Total Months {counter}\n'
    avgChange = f'Average Change: ${average_diff}\n'
    grtIncrease = f'Greatest Increase in Profits: {max_date} $%.0f \n'%max_diff
    grtDecrease = f'Greatest Decrease in Profits: {low_date} $%.0f \n'%low_diff
  
    Output = header + divider + ttlMonths + total + avgChange + grtIncrease + grtDecrease
    print(Output)
    
with open("Analysis/FinancialAnalysis.txt", "w") as f:
    f.write(Output)
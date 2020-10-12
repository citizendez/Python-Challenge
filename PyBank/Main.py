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


# %% the code
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
        diff = profit_loss - prev #The greatest increase in profits (date and amount) over the entire period
        prev = profit_loss
        if diff > max_diff:
            max_diff = diff
            max_date = row[0]
    #print(max_diff)
    #print(max_date)
        if diff < low_diff: #The greatest decrease in losses (date and amount) over the entire period
            low_diff = diff
            low_date = row[0]
        if counter > 1:   #The average of the changes in "Profit/Losses" over the entire period
            total_diff += diff
    #print(low_diff)
    #print(low_date)

    average_diff = round(total_diff/counter, 2)
    print(average_diff)
    

  
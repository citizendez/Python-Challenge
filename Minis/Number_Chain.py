# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:48:54 2020

@author: citiz
"""
Q_One = int(input('How many numbers?'))
Q_Two = 'y'
run = "y"
Exit = 'n'
running_count = 0

while Q_Two == run:
    count = 0
    while count < Q_One:
        print(running_count)
        count = count + 1
        running_count = running_count + 1
        
    Q_Two = input('Would you like to continue y or n?')
    if Q_Two == run:
        Q_One = int(input('How many numbers?'))
    
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:16:00 2020

@author: citiz
"""
# %% inrto to pie store with menu items numbered
#pies = ['(1) Pecan', '(2) Apple Crisp', '(3) Bean', '(4) Banoffee',  '(5) Black Bun', '(6) Blueberry', '(7) Buko', '(8) Burek',  '(9) Tamale', '(10) Steak']

print('Welcome to the House of Pies! Here are our pies:')
print('-------------------------------------------')
pies = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee',  'Black Bun', 'Blueberry', 'Buko', 'Burek',  'Tamale', 'Steak']
menu = ''
for pie in pies:
    num = pies.index(pie)+1 
    menu = menu + f"({num}) {pie}, "
    #print(f'({num}){pie},')
print(menu)
    
# %% reorder loop
x = 'yes'
total = []
pie_order_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


while x == 'yes':
    order = int(input('What pie would you like to order? Please select pie number')) - 1
    total.append(pies[order])
    pie_order_count[order] += 1
    x = input(f"Great! We'll have that {pies[order]} right out for you. Would you like to make another order?")

for index in range(0, len(pies)):
    print(f'{pie_order_count[index]} {pies[index]}')

#print(f"Your total order is: {len(total)}")
#print(pie_order_count)
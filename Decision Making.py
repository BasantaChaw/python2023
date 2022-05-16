# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:33:55 2022

@author: Ibasanta Chaw
"""

# Python Decision Making (Conditionnal Statements )

var = 100
if var:
    print('House full')
    print('Ticket Price', var)
# -----------------------------------------------
age = 20
if age >= 20:
    print('Welcome !')
else:
    print('Soryy !')

# -----------------------------------------------

var1 = 4
list = ['Sunday', 'Monday', 'Tuesdat',
        'Wenesday', 'Thursday', 'Friday', 'Saturday']
print()
print('Week Name :')
if var1 == 1:
    print(list[0])
elif var1 == 2:
    print(list[1])
elif var1 == 3:
    print(list[2])
elif var1 == 4:
    print(list[3])
elif var1 == 5:
    print(list[4])
elif var1 == 6:
    print(list[5])
elif var1 == 7:
    print(list[6])
# ---------------------------------------------------

# wap to find largest number among then 3 numbers in python

a = 121
b = 23
c = 721
if a > b:
    if a > c:
        print('largest Number Is A = ', a)
    else:
        print('largest Number Is C = ', c)
elif b > c:
    print('largest Number Is B = ', b)
else:
    print('largest Number Is C = ', c)
#---------------------------------------------------

#wap to find the given number Is even or odd

a=12
if a%2==0:
    print('Evne Number !')
else:
    print('Odd Number !')
    
#---------------------------------------------------


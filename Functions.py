# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:26:20 2022

@author: Ibasanta Chaw
"""


def prints():
    print('Hello, Basanta Vhaw')


prints()
# ------------------------------------------

# wap to find largest number using functions


def largest(x, y):
    if x > y:
        return x
    else:
        return y


a = 1221
b = 131
c = 34
d = largest(a, b)
e = largest(c, d)
print('The Largest Number Is :', e)


# -----------------------------------------------------------

def about(x):
    print('My Name Is :', x)

about('Basanta Chaw')

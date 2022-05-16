# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:52:42 2022

@author: Ibasanta Chaw
"""
# @choice
#Python- Numbers
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = random.choice(list)
print(k)
print('-------------------------')
# ----------------------------------------------
k = random.randrange(1, 50, 5)
print(k)
print('random selected : ', random.randrange(100))
# ----------------------------
print('Random ', random.random())
# ---------------------------------
# @shuffled list elemnet
print('-------------------------')
list = ['Basanta', 'Ritu', 'Sapana', 'Indu']
random.shuffle(list)
for var in list:
    print(var)
import math
print(math.sin(60))
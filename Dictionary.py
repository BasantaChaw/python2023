# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:51:04 2022

@author: Ibasanta Chaw
"""

# PythoN-Dictionary

dict = {'Fname': 'Basanta', 'Lname': 'Chaw',
        'Age': 20, 'Gender': 'Male', 'contact': 980899}
dict2 = dict.copy()
print(dict2)
print('----------------------------')
print(dict.get('Lname'))
print('----------------------------')
print(dict2.items())
print('------------------')
print(dict2.keys())
print('------------')
print(dict2.values())

# ----------------------------------
# update
dict3 = {'car': 'audi', 'price': 2000}
dict2.update(dict3)
print(dict2)

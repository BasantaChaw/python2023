# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:53:24 2022

@author: Ibasanta Chaw
"""
# Basic Oprators in Python language


# ---------------------------------------------------------
# 1.> Python Arithmetic Operators
# ---------------------------------------------------------

num1 = 12
num2 = 34
print('Add Any two Numbers Is :', num1+num2)
print('Subract Any two Numbers Is :', num1-num2)
print('Multiply Any Two Numbers Is : ', num1*num2)
print('Divided Any Twio Numbers Is : ', num1/num2)
print('Modulus Any Two Numbers Is :', num1 % num2)
print('Exponent Any Two numbers Is :', 2**4)
print('floor Divided Any Two Numbers Is : ', 9//3)


# ---------------------------------------------------------
# 2.> Python Comparison operators
# ---------------------------------------------------------

num = 'true'
ab = 'false'
if num == ab:
    print('True')
else:
    print('False')


if num != ab:
    print('True')
else:
    print('False')

if 10 > 3:
    print('Greater')
else:
    print('less')
if 10 < 3:
    print('Greater')
else:
    print('Less')

if 10 >= 10:
    print('hi')
else:
    print('helo')


# ---------------------------------------------------------
# 3.> Python Assignment Operators
# ---------------------------------------------------------


a = 12
b = 23
a += b
print(a)
a -= b
print(a)
a *= b
print(a)


# ---------------------------------------------------------
# 4.> Python Logical Operators
# ---------------------------------------------------------

user = 'basanta'
passs = 'chaw'
if (user == 'basanta' and passs == 'chaw'):
    print('Successfully')
else:
    print('Unsuccessfully !')

if user == 'basanta' or passs == 'chaw1':
    print('successfully !')
else:
    print('Unsuccessfully')
if not(user and passs):
    print('successfully')
else:
    print('Unsuccessfully')


# ---------------------------------------------------------
# 5.> Python Membership Operators
# ---------------------------------------------------------

list = ['basanta', 'ritu', 'anuragh', 'indu']
list1 = ['subash', 'basanta', 'biky', 'sunil']
if list[0] in list1[1]:
    print('persona is here!')
else:
    print('person is not here !')

if list[0] not in list1[1]:
    print('persona is here!')
else:
    print('person is not here !')


# ---------------------------------------------------------
# 6.> Python Identity Operators
# ---------------------------------------------------------

a = 12
b = 13
if a is b:
    print('A is Equal To The B !')
else:
    print('A Is Not Equal To The B !')

if a is not b:
    print('true')
else:
    print('False')


# ---------------------------------------------------------
# 7.> Python Precendence Operators
# ---------------------------------------------------------
a = 20
b = 10
c = 15
d = 5
print("a:%d b:%d c:%d d:%d" % (a, b, c, d))
e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ", e)
e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ", e)

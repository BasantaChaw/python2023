# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:07:08 2022

@author: Ibasanta Chaw
"""

# Python loops
# While loop
count = 0
num = 12
while count < num:
    print('Basanta Chaw')
    count += 1


# --------------------------------------------------
count = 0
while count < 5:

    print(count, " is less than 5")
    count = count + 1
else:

    print(count, " is not less than 5")

# ----------------------------------------------------
# for loop
a = 10
for var in (range(a)):
    print(var)
num = 11
for var in range(1, num):
    print('Basanta chaqw', var)

# -----------------------------------------------------

num = 50
gap = 10
for var in range(1, num, gap):
    print(var)
# ---------------------------------------------------
print('---------------------------')
list = [12, 423, 4, 2, 34, 4, 3, 2, 1, 3, 4]
for var in list:
    print(var)

print()

# -------------------------------------------------------
list = ['banana', 'apple', 'black berry', 'craps', 'papaya']
for var in list:
    print(var)
# ------------------------------------
str = 'Python'
for var in str:
    print(var)

# --------------------------------------
# find the lenth of list elemets\
print('-----------------------------')
list = [12, 32, 43, 2, 34, 2, 21]
for var in range(len(list)):
    print(var)
# ----------------------------------------

# using break
for var in range(4):
    if var == 5:
        print('matched')
        break
else:
    print('Doestnit have even number')
# -----------------------------

# nested for loop

for var in range(1, 11):
    for var1 in range(1, 11):
        k = var*var1
        print(k, end=' ')
    print()
# --------------------------------------------

for letter in 'python':
    if letter == 'h':
        pass
        print('hi')
    print('hello')
# --------------------------------------------

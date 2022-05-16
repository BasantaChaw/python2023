# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:30:03 2022

@author: Ibasanta Chaw
"""

# Python-List
# 1.> append
list = [12, 31, 3, 544, 34, 12, 32, 4, 12]
add = 'basanta'
list.append(add)
print(list)
# --------------------------------

# 2.> Count\
print()
k = list.count(12)
print(k)
# -----------------------------
#3.> extends
list1 = ['indu', 'ritu', 'sapana']
list.extend(list1)
print(list)
# ---------------------------------
# 4> index nu,ber
print(list.index(34))
# _-------------------------
# 5.> insert data
list.insert(12, 'Chaw')
print(list)
# -------------------------------------
#6.> Pop

list.pop(12)
print(list)

# --------------------------------------
#7.> Remove
list.remove('sapana')
print(list)
# ------------------------------------
# 8.,> reverse
print('---------------------------')
list.reverse()
print(list)
# -------------------------------------

#9.> sort
print('--------------------------------------')
list2 = [22, 4234, 54, 32, 21, 3, 1, 1322, 4323]
list2.sort()
print(list2)

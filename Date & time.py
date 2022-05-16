# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:04:17 2022

@author: Ibasanta Chaw
"""

# Python Date And Time
import calendar
import time
localtime = time.localtime(time.time())
print(localtime)
# ------------------------------------

cal = calendar.month(2023, 1)
print(cal)
print('------------------------')
# _----------------------------------

print('time.altzone : ', time.altzone)
times = time.localtime()
print('asctime :', time.asctime(times))
print()
# ------------------------------------------

print('ctime :',time.ctime())
import time
print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())
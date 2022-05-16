# -*- coding: utf-8 -*-
"""
Created on Sun May 15 09:02:28 2022

@author: Ibasanta Chaw
"""

try:
    fh = open('TextFile.txt', 'w')
    fh.write('Hi how aree u hhhhh')
except IOError:
    print('error')
else:
    print('successfully')
    fh.close()


try:
    ph=open('text.txt','w')
    ph.write('my name is basanta chaudhary')
finally:
    print('eroor')
    ph.close()
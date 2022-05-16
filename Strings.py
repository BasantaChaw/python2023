# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:14:04 2022

@author: Ibasanta Chaw
"""

#Python Strings
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str.capitalize())
print()
print()
print(para_str.upper())
print(para_str.lower())
print(para_str.title())
print(para_str.replace('this','basanta'))
print(para_str.rstrip())
print(para_str.count('a'))
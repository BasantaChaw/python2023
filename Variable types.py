# -*- coding: utf-8 -*-
"""
Created on Sat May 14 17:14:13 2022

@author: Ibasanta Chaw
"""
# wap to print many types of variable of python using and display

# Display data aboout of car
counter = 100
miles = 10000.0
name = 'Basanta Chaw'
print(counter)
print(miles)
print(name)

# ----------------------------------------------------------
st1 = 'Basanta Chaw'
st2 = 'Anuragh Baitha'
st3 = 'Rituraj'
salary1 = salary2 = salary3 = 30000.0
print('-------Name------')
print(st1+'  '+st2+'  '+st3)
print('-------Salary-----')
print(str(salary1)+'  '+str(salary2)+'  '+str(salary3))


#---------------------------------------------------------
# 1.> Python Strings
#---------------------------------------------------------


str='Basanta Chaw'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+" Ritu")


#---------------------------------------------------------
# 2.> Python Lists
#---------------------------------------------------------

list=['Basanta','Ritu',69,96,'ús',10.7]
list1=[12,'ab',88]
print(list)
print(list1)
print(list[0])
print(list[2:4])
print(list[2:])
print(list[2:-1])
print(list*3)
print(list+list1)



#---------------------------------------------------------
# 3.> Python Tuples
#---------------------------------------------------------

tuple=('Basanta','Ritu','Anuragh',12,32,57.5)
tuple1=('abs',232,3,'ib')
print(tuple)
print(tuple1)
print(tuple[0])
print(tuple[3:5])
print(tuple[:5])
print(tuple*4)
print(tuple+tuple1)

 

#---------------------------------------------------------
# 4.> Python Dictionary
#---------------------------------------------------------


dict={}
print(dict)
dict['one']='This is my book'
dict[2]='This my phone not your !'

tinydict={'bookname':'Python','Price':1000,'Date':'apr 23'}

print(dict['one'])
print(dict[2])
print(tinydict['bookname'])
print()
print(tinydict.keys())
print(tinydict.values())

#functions 

print(chr(65))
print(UnicodeWarning(4))
print(ord('A'))
print(hex(5))
print(oct(34))
print(repr('Basanta'))

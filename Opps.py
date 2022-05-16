# -*- coding: utf-8 -*-
"""
Created on Sun May 15 09:12:49 2022

@author: Ibasanta Chaw
"""

# using Oops concepts in python


class Employee:
    emcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emcount += 1

    def displayCount(self):
        print('Total Employee : ', Employee.empcount)

    def displayEmployee(self):
        print('Name :', self.name, ' Salalry : ', self.salary, ' ')


emp = Employee('Zara', 122)
emp1 = Employee('Basanta', 1222)
emp.displayEmployee()
emp1.displayEmployee()
print('Count ', Employee.emcount)
# -------------------------------------------------------
print('---------------------------------------------')\


# ---------------------------------------------------


class employee:
    count = 0

    def __init__(self, names, sex, salaries):
        self.names = names
        self.sex = sex
        self.salaries = salaries
        employee.count += 1

    def displays(self):
        print('Name : ', self.names, ' Sex : ',
              self.sex, ' Salary : ', self.salaries)


emp1 = employee('Basanta chaw', 'm', 30000)
emp2 = employee('Ritu chaw', 'm', 15000)
emp3 = employee('Anuragh', 'm', 120000)
emp4 = employee('indu', 'f', 12000)
emp1.displays()
emp2.displays()
emp3.displays()
emp4.displays()
print('Total Employess : ', employee.count)
print('----------------------------------------')
print('Employee.__doc__:', employee.__doc__)
print('Employee.__name__:', employee.__name__)
print('Employee.__Module__:', employee.__module__)
print('Employee.__bases__:', employee.__bases__)
print('Employee.___dict__:', employee.__dict__)


# _--------------------------------------------------

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, 'Destroy')


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3


# inheritance class in python

print('------------------------------------------')


class Parent:
    parentAttr = 100

    def __init__(self):
        print('Calling Parent Constructor')

    def ParentMethod(self):
        print('calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent Attr :', Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print('calling child constructor')

    def childMethod(self):
        print('calling child method')


c = Child()
c.childMethod()
c.setAttr(200)
c.getAttr()


# ----------------------------------------------------
print('-----------------------------------------')


class Parent1:
    def mymethod(self):
        print('calling parent method')


class Child1:
    def mymethod(self):
        print('calling child method')


c1 = Child1()
c1.mymethod()

# _----------------------------------------


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a+self.a, self.b+self.b)


v1 = Vector(2, 3)
v2 = Vector(5, -7)
print(v1+v2)
Vector(3, 6)


# --------------------------------------------------------
class Justcounter:
    __secretcount = 0

    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)


counter = Justcounter()
counter.count()
counter.count()
print(counter.__secretcount)

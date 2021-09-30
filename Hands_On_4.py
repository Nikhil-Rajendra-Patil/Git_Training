#!/bin/python3

import math
import os
import random
import re
import sys

class Employee:
    def __init__ (self,name,id,age,gender):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender

class Organisation:
    def __init__ (self,org_name,emp_list):
        self.org_name = org_name
        self.emp_list = emp_list
    
    def addEmployee(self,name,id,age,gender):
        self.emp_list.append(Employee(name,id,age,gender))
        
    def getEmployeeCount(self):
        return len(self.emp_list)
    
    def findEmployeeAge(self,id):
        for i in self.emp_list:
            if i.id == id:
                return i.age
        return -1
    
    def countEmployees(self,age):
        count = 0
        for i in self.emp_list:
            if i.age > age:
                count += 1
        return count

if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))

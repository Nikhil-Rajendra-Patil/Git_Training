import math
import os
import random
import re
import sys

class Student:
    def __init__(self,roll,name,marks_list):
        self.roll = roll
        self.name = name
        self.marks_list = marks_list
    
    def calculate_percentage(self):
        percentage = sum(self.marks_list)//len(self.marks_list)
        return percentage
        
    def find_grade(self):
        percentage = self.calculate_percentage()
        if percentage>=80:
            return 'A'
        elif percentage>=60:
            return 'B'
        elif percentage>=40:
            return 'C'
        else:
            return 'F'

if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())

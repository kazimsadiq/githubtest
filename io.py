#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:35:32 2020
Reading and writing a file

@author: fali
"""
# keyword with - good to use, releases the 
# resources used after the snippet of the 
# code is executed! so we don't have to 
# worry about closing the file, releasing the 
# grades resource!
# with open('grades.txt', mode='w') as grades:
#     grades.write('100 John_Doe_1 98\n')
#     grades.write('101 John_Doe_2 93\n')
#     grades.write('102 John_Doe_3 95\n')
#     grades.write('103 John_Doe_4 88\n')
#     grades.write('104 John_Doe_5 89\n')
#     grades.write('105 John_Doe_6 88\n')
    

with open('grades.txt', mode='r') as grades:
    for grade in grades:
        x, y, z = grade.split()
        # print (x,y,z)
        x = grade.split()
        # print(f"Student id: {x} name: {y} grade: {z:>10.2s}")
        print(x)
        
        
        
    



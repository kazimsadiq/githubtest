#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:05:47 2020

@author: fali
"""


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def printname(self):
    print(self.name, self.age)
    
p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
#p1.printname()

class Account:
   def __init__(self, name, balance):
    self.name = name
    if balance < 0:
        raise ValueError("cannot be less than 0")
    self.balance = balance 
    
   def my_balance(self):
       print(f"Balance is {self.balance}")
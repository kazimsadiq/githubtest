#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:56:56 2020

@author: fali
"""


try:
    print(10/0)      # if executes successfully only else and finally will execute
except ValueError: 
    print("value error")
except FileNotFoundError: 
    print("file not found")  
except:
    print('unhandled error')
finally:     # always execute
    print("finally we are here")





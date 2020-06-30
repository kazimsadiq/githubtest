# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("Hello World updated - new commit")

def fib(n):
    a, b =0, 1
    counter = 1
    while counter <n:
        print (a, end=' ')
        a, b = b, a+b
        print()
        counter += 1
        
    print(__name__)
    return(0)
    
fib(20)    


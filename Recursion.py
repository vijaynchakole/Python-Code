# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 05:13:04 2020

@author: hp
"""


import sys

sys.getrecursionlimit() # 3000

# change recursion limit to 5000

sys.setrecursionlimit(5000)

sys.getrecursionlimit() #5000



# Recursion function which goes infinite recursive calls
i = 1
def fun():
    global i
    print("inside fun ", i )
    i = i + 1
    fun()

fun()

# Recursive function which performs recursive calls 10 times 

def gun():
    global i
    if i<=10:
        i = i + 1
        print("inside gun ", i)
        gun()
        
        
gun()




def factorial(val):
    
    if(val==0):
        return 1
    
    return val * factorial(val - 1)
    
factorial(5)

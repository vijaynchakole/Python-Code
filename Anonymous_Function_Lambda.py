# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 04:41:50 2020

@author: hp
"""

# normal function
 
def add(a, b):
    return(a+b)
    
    
num1 = 5
num2 = 8

result = add(num1, num2)
result

##############################################################################

# using lambda function

result2 = lambda no1,no2 : no1 + no2

print(result2(num1, num2))

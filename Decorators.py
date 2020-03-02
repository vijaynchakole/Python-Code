# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:35:57 2020

@author: hp
"""

def substraction(a, b):
    return (a - b)


def decorator(originalFunction):
    def updator(a, b):    
        if (a < b) :        
            a, b = b, a        
        return originalFunction(a, b)
    return updator 


newsubstract = decorator(substraction)

print("Substraction of 10 and 7 is ", newsubstract(10, 7))


print("Substraction of 7 and 10 is ", newsubstract(7, 10))


###############################################################################


# addiction and multiplication,  each number multiply by 10 before addition

def add(a, b):
    return(a + b)
    
    

def decorator(originalFunction):
    def updator(a, b):
        a, b = (a * 10), (b * 10)
        return originalFunction(a, b)
    return updator


newadd = decorator(add)

print("addition of 5 and 4 ", newadd(5, 4))

    
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:07:21 2020

@author: hp
"""

# function which accept nothing and return nothing

def nothing():
    print("inside nothing ")
    
    
# function which accept value and return nothing
    
def accept1value(value):
    print("inside accept1value")
    
# function which accept value and return value

def accept_return(value):
    print("inside accept_return")
    return (value + 10)

# function accept multiple values and return multiple values

def accept_return_more_value(num1, num2):
    print("inside accept_return_more_value")
    return (num1*2, num2*2)


# function which call another function which is defined outside it


def naked():
    print("inside naked ")
    
def outer():
    print("inside outer ")
    naked()
    
# function which call another function which is defined inside it (nested function)
    
def outer_function():
    print("inside outer function ")
    number = 10
    def inner():
        
        print("inside inner function")
        print(number)
    inner()
    
    

nothing()
accept1value(10)
accept_return()
accept_return_more_value(10, 20)
naked()
outer()
outer_function()


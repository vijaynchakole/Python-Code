# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 04:06:47 2020

@author: hp
"""

MyList = [8,9,5,16,2,4,21,30,11]
type(MyList)


# Filter Map Reduce using lambda function

# Filter function is used to filter out out data as per our requirment
# here we want only even number so filter function will return all even number from our data
# return value of filter function is list

EvenList = list(filter(lambda no : (no%2 == 0), MyList))
type(EvenList)
EvenList

#Map function will add 2 in each number in our EvenList and then return it

Modified_list = list(map(lambda no : (no + 2), EvenList))
type(Modified_list)
Modified_list


# After applying reduce function our sum contains addition of all elements from ModArray ie 70 


import functools as ft

final_sum = ft.reduce(lambda a,b : a+b, Modified_list)
final_sum


#################################################################################

# filter map reduce using user defined function

MyList = [8,9,5,16,2,4,21,30,11]

def evenChk(no):
    return(no%2 == 0)
    
def Increase(no):
    return(no+2)

def sum(a, b):
    return(a+b)
    
    
even_list = list(filter(evenChk, MyList))
even_list


modified_list = list(map(Increase, even_list))
modified_list


summation = ft.reduce(sum, modified_list)
summation

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 04:53:26 2020

@author: hp
"""

import functools as ft

def AcceptData():
    size = int(input("enter number of elements "))
    
    ls = list()
    
    for i in range(size):
        ls.append(int(input("enter number ")))
    
    return ls


print(AcceptData())


def EvenChk(no):
    return(no%2==0)
    
    
def Modify(no):
    return (no+2)

def Add(no1, no2):
    return(no1 + no2)
    
    

data = AcceptData()

filter_data = list(filter(EvenChk, data))

modified_data = list(map(Modify, filter_data))

result = ft.reduce(Add, modified_data)

print(result)    
    

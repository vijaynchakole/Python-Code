# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:07:10 2020

@author: hp
"""

# create object of list

ls = list()

#Ask user for number of elements in list

num = int(input("enter number of elements in list "))

for i in range(num):
    value = int(input(" num " ))
    ls.append(value)
    

print("elements of list's are ", ls)

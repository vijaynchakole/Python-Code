# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 04:18:42 2020

@author: hp

"""


"""
Python provides numerous built-in functions that are readily available to us at the Python prompt. Some of the functions like input() and print() are widely used for standard input and output operations respectively 
We use the print() function to output data to the standard output device (screen). 
By using Input function we can accept input from standard input device ie Keyboard. 

"""




print("Hello World\n")
print("New ERA")

X = input()    # 8
Y  = input()   # 3

print(X + Y) # 83 because default datatype is string hence
# it concatinate X and Y that is become 83

# typecasting to integer

X = int(input("enter first number "))  # 9
Y = int(input("enter second number ")) # 6

print(X + Y) # 15
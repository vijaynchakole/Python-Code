# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:21:46 2020

@author: hp
"""

"""
Duck Typing is a way of programming in which an object passed into a function or
method supports all method signatures and attributes expected of that object at run time.
The object's type itself is not important.
•Rather, the object should support all methods/attributes called on it.
For this reason, duck typing is sometimes seen as "a way of thinking rather than a type system". 

In duck typing, we don't declare the argument types in function prototypes or methods.
 This implies that compilers can't do type checking. 

"""


class Sparrow:
    def fly(self):
        print("Sparrow is flying ")
        

class Airplane:
    def fly(self):
        print("Airplane is flying ")
        
        
class Whale:
    def swim(self):
        print("Whale in swimming ")
        
        

#type of entity is no specified
# we expect entity to have a callable named fly at run time
        
def fun(entity):
    entity.fly()
    
    
    
sparrow_obj = Sparrow()
airplane_obj = Airplane()
whale_obj = Whale()

fun(sparrow_obj)  # Sparrow in flying
fun(airplane_obj)  # Airplane is flying
fun(whale_obj)  # error 'Whale' object has no attribute "fly""


# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 05:36:59 2020

@author: hp
"""

class demo:
    
    def __init__(self,no1,no2):
        self.i = no1
        self.j = no2
        
    def multiply(self):
        print("inside multiply ")
        
        print(self.i * self.j)
        
    def add(self):
        print("inside addition ")
        print(self.i + self.j)
        
# creating object for demo class
        
obj1 = demo(10, 30)
obj1.multiply()
obj1.add()


obj2 = demo(5,6)
obj2.multiply()
obj2.add()


################################################################################

# Characteristics
# there are two types of variables as 
# 1.Instance variable 
# 2.Class variable  

class demo2:
    x = 10
    def __init__(self,no1,no2):
        self.i = no1
        self.j = no2
    
    
obj1 = demo2(10,30)
obj1.i
obj1.j
obj1.x
demo2.x


obj2 = demo2(50,60)
obj2.i
obj2.j
obj2.x
demo2.x

###############################################################################

#Behaviours of Class 

"""
 there are three types of methods as 
 1.Instance method 
 2.Class method 
 3.Static method
 
 """
 
 
 
    
    
    

class demo3:
    
    def __init__(self):
     self.i = 10
     self.j = 20
    
    def fun(self):
        print("inside instance method fun ")
        
    
    @classmethod
    def gun(cls):
        print("inside class method")
        
    @staticmethod
    def sun():
        print("inside static method")
     
 
         
    
    
    

obj3 = demo3()
obj3.fun()        
demo3.gun()
demo3.sun()

x= 25
y=4
x//y
x%y

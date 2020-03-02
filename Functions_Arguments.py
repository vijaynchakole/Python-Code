# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:33:37 2020

@author: hp
"""

"""
Default arguments : Python has a different way of representing syntax and 
default values for function arguments. 
Default values indicate that the function argument will take that value 
if no argument value is passed during function call.  
The default value is assigned by using assignment (=) operator

"""

# default argument 

def Batches1(number = 10 , name = 'Human being'):
    print(number)
    print(name)



Batches1() # without passing any argument
Batches1(25)
Batches1(36,'Vijay')
Batches1(name = 'right',number = 36)

def Batches2(number, name = 'Human being'):
    print(number)
    print(name)


Batches2(1000)
Batches2(256, 'hello world')



def Batches3(number = 10, name ): # SyntaxError: non-default argument follows default argument
    print(number)
    print(name)
    
# SyntaxError: non-default argument follows default argument

"""
Required arguments / Position Argument :
Required arguments are the mandatory arguments of a function. 
These argument values must be passed in correct number and order during function call. 

"""

# Position Argument
def Batches5(name, fee):
    print(name)
    print(fee)

Batches5('world') # TypeError: Batches5() missing 1 required positional argument: 'fee'
Batches5(89, 'Hello')
Batches5('world', 96)

"""
Keyword arguments : Keyword arguments are relevant for Python function calls.  
The keywords are mentioned during the function call along with their corresponding values. 
These keywords are mapped with the function arguments 
so the function can easily identify the corresponding values even
if the order is not maintained during the function call. 

"""

# Keyword argument

def Batches4(name, fee):
    print(name)
    print(fee)
    
Batches4(fee = 4000, name = 'vijay')


"""
Variable number of arguments: This is very useful 
when we do not know the exact number of arguments that will be passed to a function. 
Or we can have a design where any number of arguments can be passed based on the requirement. 

"""

# Variable Number of Argument 

def Add(*no):
    ans = 0
    for i in no:
        ans = ans + i
    return ans


result = Add(10,20,30,40,50,60)

print(result)

result2 = Add(20, 30)
print(result2)



# Keyword Variable number of argument 

def StudentInfo(**other):
    print(other)
    for i, j in other.items():  # i stores keywords and j stores values
        #print(i)
        print(i,j)
        #print(j)
        
    
StudentInfo(age = 28, adress = 'PUNE', name = 'Unknown')

    
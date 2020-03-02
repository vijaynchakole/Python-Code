# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:36:25 2020

@author: hp
"""

"""
The Pool class 
Another and more convenient approach for simple parallel processing tasks is provided by the Poolclass. 
There are four methods that are:
    • Pool.apply 
    • Pool.map 
    • Pool.apply_async 
    • Pool.map_async
 The Pool.apply and Pool.map methods are basically equivalents
    to Python’s inbuilt apply and map functions. 

"""


#  below program which uses serial processing approach 

def square(num):
    return(num*num)
    
    
ls = [2,6,7,8,9,10]

result = list()

for i in ls :
    result.append(square(i))
    
    
print(result)


"""
 In above example for each number sequentially square function gets called.
 In this application only single process gets executed on one core of our CPU. 
 
 """
###############################################################################

 
# To use power of multicore processor we use Pooling in Python

# below program which uses Pooling for Parallel Programming 

import multiprocessing
import os

def square2(num):
    print(f"worker process ID for : {num} is {os.getpid()} ")
    return(num*num)

    
    
if __name__ == "__main__":
    ls2 = [2,4,3,5,7,6]
    
    # creating pool object
    p = multiprocessing.Pool()
    
    # map list to target function
    
    result = p.map(square2, ls2)
    
    print("square of each element ")
    
    print(result)



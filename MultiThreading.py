# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:54:16 2020

@author: hp
"""

import threading

value = 10 
value

def fun(number):
    global value
    value = 50
    print("inside fun ")
    for i in range(number):
        print(i)
        
        
def gun(number):
    print("inside gun")
    for i in range(number):
        print(i)


number = 5
thread_1 = threading.Thread(target = fun, args = (number,))
thread_2 = threading.Thread(target = gun, args = (number,))

# Will execute both in parallel

thread_1.start()
thread_2.start()

# join threads back to parent process

thread_1.join()
thread_2.join()

value

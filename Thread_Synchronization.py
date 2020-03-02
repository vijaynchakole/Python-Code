# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 04:16:08 2020

@author: hp
"""

import threading

amount = 0

def Counter(fun, lock):
    fun(lock)
    

def Credit(lock):
    
   
    value = int(input("enter amount for credit"))
    lock.acquire()
    global amount
    amount += value
    print("Updated Balance  : ", amount)
    lock.release()
     

def Debit(lock):
    
    value = int(input("enter amount for withdraw"))
    lock.acquire()
    global amount
    if value < amount :
        amount -= value
        print("Amount withdrawn : ", value)
    else:
        print("unable to withdraw")
        
    
    print("Available Balance  : ", amount)
    lock.release()
    


lock = threading.Lock()

thread_1 = threading.Thread(target = Counter, args = (Credit, lock,))
thread_2 = threading.Thread(target = Counter, args = (Debit, lock,))


thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()    

"""
In above application at a time only one thread gets executed. 
If any of the above thread gets scheduled it acquires lock and at that time other thread has to wait.
 
""" 
    
    


     
    
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:21:16 2020

@author: hp
"""

from os import *
from threading import Thread
from multiprocessing import *
from time import *


def Square(no):
    print(getpid())
    return (no*no)

ls_1 = [1,31,41,3,5,4,2]

ls_2 = list()

start_time = time()

for i in range(len(ls_1)):
    ls_2.append(Square(ls_1[i]))

end_time = time()

print(ls_2)

print("serial programming time taken : ",end_time - start_time)


pobj = Pool()

start_time_2 = time()

ls_3 = pobj.map(Square, ls_1)

end_time_2 = time()

print(ls_3)

print("parallel programming time taken : ", end_time_2 - start_time_1)
print("parallel : ", getpid())

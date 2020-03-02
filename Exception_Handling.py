# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 04:50:55 2020

@author: hp
"""

no1 = int(input("enter first number "))
no2 = int(input("enter second number "))


try:
    ans = no1 / no2
    print(ans)
except ZeroDivisionError :
    print("Unable to divide by Zero")

finally:
    print("inside finally block to release all resources ")


print("End of the Exception handling application")
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 06:43:44 2020

@author: Vijay Narsing Chakole

"""


class AgeInvalid(Exception):
    def __init__(self, name_exception):
        self.value = name_exception



def main():
    num = int(input("enter your Age "))
    try:
        if num<18:
            raise(AgeInvalid("Invalid Age : under age"))
        print("Your Age is Above 18...")
    except AgeInvalid as ex:
        print(ex.value)

if __name__ == "__main__":
    main()
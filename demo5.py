# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:30:14 2020

@author: Vijay Narsing Chakole

Absolute and Relative Pathnames in UNIX
A path is a unique location to a file or a folder in a file system of an OS.A path to a file is a combination of / and alpha-numeric characters.

Absolute Path-name

An absolute path is defined as the specifying the location of a file or directory from the root directory(/).
To write an absolute path-name:



Start at the root directory ( / ) and work down.
Write a slash ( / ) after every directory name (last one is optional)


An absolute path is defined as specifying the location of a file or directory from the root directory(/).
In other words,we can say that an absolute path is a complete path from start of actual file system from / directory.


*******************************************************************************
Relative path

Relative path is defined as the path related to the present working directly(pwd).
It starts at your current directory and never starts with a / .


"""

from sys import *
import os


def DirectoryWatcher(path):
    # input parameter path is folder name must be
    # flag = os.path.isabs(path)

    path = "Automation"
    path = os.path.abspath(path)
    exists = os.path.isdir(path)
    exists

    if exists == True:
        for folder_name, sub_folder, file_name in os.walk(path):
            print("Current folder name : ", folder_name)

            for sub_fold in sub_folder:
                print("sub folder of " + folder_name + "is" + sub_fold)

            for fileName in file_name:
                print("File inside " + folder_name + " is " + fileName)
                print('')

    else:
        print("invalid path")


def main():
    print("second argument " + argv[1])
    print(type(argv[1]))

    try:

        DirectoryWatcher(argv[1])

    except ValueError:
        print("incorrect datatype in input")

    except Exception as E:
        print(E)









def DirectoryWatcher(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filename in os.walk(path):
            print("Current folder is ", foldername )
            for subfold in subfolder :
                print("sub Folder of " + foldername +" is "+ subfold)
            for file_name in filename:
                print("File inside "+foldername+" is "+file_name)
            print('')
    else:
        print("Not Found ")












"""    
     path = os.path.abspath("Automation")
     path
     exists = os.path.isdir(path)
     exists
     if exists :
         for folder_name, sub_folder, file_name in os.walk(path):
                print("Current folder name : ", folder_name)

                for sub_fold in sub_folder :
                    print("sub folder of "+ folder_name+ "is" + sub_fold)

                for fileName in file_name :
                    print("File inside "+folder_name+ " is " +fileName)
                print('')

     else :
         print("invalid path in main")


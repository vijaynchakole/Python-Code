# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 05:23:00 2020

@author: hp

There are different data types in python as
 •None
 •Numeric -> int, float, bool, complex
 •Sequence -> List, Tuple, Set, String, Range •Dictionary 
 
"""

no = None
print(no)
print(type(no))
print(id(no))

num = 10
print(num)
print(type(num))
print(id(num))


fnum = 3.14
print(fnum)
print(type(fnum))
print(id(fnum))


fnum = int(fnum)

print(fnum)
print(type(fnum))
print(id(fnum))


# we can convert one datatype to another datatype (typecasting)

num = 20
print(num)
print(type(num))
print(id(num))

# we can convert one datatype to another datatype (typecasting)
num = float(num)
print(num)
print(type(num))
print(id(num))


# under Sequence there are different data types as List, Set, Tuple, Range

listex = [10,20,30,40,50]

print(listex)
print(type(listex))

Setex = {10,20,30,40}
print(Setex)
print(type(Setex))


TupleEx = (10,20,30,40,50,60,70,80,90,100)
print(TupleEx)
print(type(TupleEx))

listex = list(range(10))
listex2 = list(range(10))

print(listex)
print(type(listex))
print(id(listex))


print(listex2)
print(id(listex2))



# Dictionary contains keys and values


batches ={'first':100, 'Second':200, "Third":300}

batches
batches.keys()
batches.values()
batches['Second']
batches['Third']


###############################################################################

# Python does not have built-in support for Arrays, but Python Lists can be used instead. 
# Array
# As there is no direct support for ARRAY in python we have to import array module to create array


import array as arr

Myarray = arr.array('i',[10,20,30,40]) # i is consider as datatype code
Myarray
type(Myarray)
Myarray[-1] # last element
Myarray[0]  # first element
Myarray[1]  # Second elemnet
Myarray.typecode
Myarray.reverse()
Myarray

for i in range(len(Myarray)):
    print(Myarray[i])


i = 0
while(i<len(Myarray)):
    print(Myarray[i])
    i+=1
    
    
    
###############################################################################
    
# List

listex = ['first','second',3, 'fourth']
len(listex)
listex[0]
listex[1]
listex[-1]
listex[1:]
listex[:3]


listex.append('fifth')
listex

listex.insert(2,'newelement')
listex

listex.remove('newelement')
listex

listex.pop()
listex

del listex[2]
listex

listex.extend(['sixth', 'seventh'])
listex

listex.sort()
listex

listex.extend([5,3,6])
listex.sort() # TypeError: '<' not supported between instances of 'int' and 'str'


###############################################################################

# Set
"""
A set is an unordered collection of items. Every element is unique (no duplicates) and
must be immutable (which cannot be changed). However, the set itself is mutable. 
We can add or remove items from it.
Sets can be used to perform mathematical set operations 
like union, intersection, symmetric difference etc. 
Set is unordered unindexed collection of Heterogeneous objects 
•Heterogeneous •Unordered •Unindexed •Immutable •Duplicate not allowed 

"""

myset = {'first',2,3.14,'last',3.14}

type(myset)
len(myset)
myset.remove(3.14)
myset

myset.discard(2)
myset
myset.add('zeroth')
myset

###############################################################################

# String

mystring = 'hello world'
mystring2 = "  New hello world  "

type(mystring)
type(mystring2)

mystring[0]
mystring[-1]
mystring[:7]
mystring[5]

## strings in python are immutable 
mystring[0] = 'B'  #TypeError: 'str' object does not support item assignment

#strip method removes whitespaces from begining and end 
mystring2.strip()

## By using split we can tokanize the strinng 
mystring2.split()
mystring2

###############################################################################

# Tuple
"""
Tuples is considered as sequance of immutable objects. 
Tuples are similar as List but it is immutable in nature.
 •Heterogeneous •Ordered •Indexed •Immutable •Allows Duplicate 

"""

tup = (11,12,13,14,15)
type(tup)
tup[0] = 100  
# TypeError: 'tuple' object does not support item assignment

tup = (11)
type(tup)
tup
tup = (30)
tup
type(tup)


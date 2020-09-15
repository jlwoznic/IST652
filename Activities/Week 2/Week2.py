#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:45:53 2020

@author: joycewoznica
"""

mp = "Today is a Great DAY"
mp.lower()
mp.upper()
mp.strip()
mp.startswith("T")
mp.find("a")


# Activity 2.2b

newstr = 'X-DSPAM-Confidence:0.8475'
vars = newstr.split(':')
num = round(float(vars[1]),2)

# lists and tuples

# list
prime_numbers = [2,3,5,6,11,13,17]

# tuple
perfect_squares = (1,4,9,16,25,36)

# display lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))
      
# Iterate over both sequences
for p in prime_numbers:
    print ("Prime: ", p)
    
for n in perfect_squares:
    print ("Square: ", n)    
    
print("List Methods")
print(dir(prime_numbers))
print (80*"-")
print("Tuple methods")
print(dir(perfect_squares))

import sys
print(dir(sys))

print(help(sys.getsizeof))

# check memory of each
list_eg = [1,2,3,'a', 'b', 'c', True, 3.14159]
tuple_eg = (1,2,3,'a', 'b', 'c', True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# tuples cannot be changed, but lists can be added, remove, changed
# tuples is faster
import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List Time: ", list_test)
print("Tuple Time: ", tuple_test)


empty_tuple = ()
test1 = ("a")
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

# instead
test1 = ("a",)
print(test1)

test1 = 1,
test2 = 1,2
test3 = 1,2,3
print(test1)
print(test2)
print(test3)

# (age, country, knows_python)
survey = (27, "Vietnam", True)
age, country, knows_python = survey
age
country
knows_python

# Exercise 2.3 Tuples
tuple1 = (1, "a", 2, "b", 3, "c")
len(tuple1)
num1, chr1, num2, chr2, num3, chr3 = tuple1
num1
chr1
num2
chr2
num3
chr3


filePath = '/Users/joycewoznica/Syracuse/IST652/Labs/Lab1/NBA-Attendance-1989.txt'

# loop through each line
with open(filePath, 'r') as nbaFile:
    for nbaLine in nbaFile:
        # strip out newlines
        nbaLine = nbaLine.strip('\n')
        # split by tabs
        nbaVars = nbaLine.split('\t')
        # remove any empty items from list created
        nbaVars = list(filter(lambda x: x!= "", nbaVars))
        # assign variables to each item in list
        team, attendance, price = nbaVars
        # print required output line
        print('Team ' + team)
        print('Attendance ' + attendance)
        print('Ticket Price $' + price)




















# -*- coding: utf-8 -*-
"""
Author: Joyce Woznica
Date: 3/28/2020
Subject: Python Exercises Week 1

This is a temporary script file.
"""
# Activity 1

x = 43
x = x + 1
print (x)

# Answer b) 44

# Activity 2
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours)*float(rate)
print("Pay: $" + str(pay))

# Activity 3

width = 17
height = 12.0

width / 2
width / 2.0
height / 3
1 + 2 * 5


# Boolean Activity
#score = float(score)
def test_score(value):
    try:
        score = float(value)
        if score >= 0.9 and score < 1.0: grade = "A"
        elif score >= 0.8 and score < 0.9: grade = "B"
        elif score >= 0.7 and score < 0.8: grade = "C"
        elif score >= 0.6 and score < 0.7: grade = "D"
        elif score < 0.6: grade = "F"
        else: grade = "Bad Score"
    except: 
        grade = "Bad Score"
    return grade

score = input("Enter Score: ")
print("Grade: " + str(test_score(score)))


# Loops Activity
# Exercise 1
samples = ["at", "c", "cat", "rat",
           "hat", "it", "fat", "smith",
           "sat", "vat"]
# loop to use this list
for item in samples:
    if len(item) > 2: print("Item is: " + item)
    
# Exercise 2
samples = ["at", "book", "c", "dog",
           "elephant", "cat", "telephone", "tv",
           "hammer", "abc"]
# loop to use this list
for item in samples:
    if len(item) > 2 and len(item) < 5: print("Item is: " + item)
    

    

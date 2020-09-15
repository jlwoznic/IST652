# Week 4
# Lab 2
# Author: Joyce Woznica
# Class: IST 652
# 
# LAB TWO:
# Dictionaries: You may wish to write the code for parts a–d in one Python file.

# Submit your code and the output of your program. Submit assignment as a .txt, .py, .pdf, or jupyter notebook file.
# Due 24 hours before the live session in Week 4.

# Data Dictionaries
# in stock grocery items
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# prices ofr items
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# a. Show the expression that gets the value of the stock dictionary at the key ‘orange’. 
oValue = stock["orange"]
oValue

#    Show a statement that adds an item to the stock dictionary called ‘cherry’ with some integer value 
stock["cherry"] = 25
stock

#    Show and that adds ‘cherry’ to the prices dictionary with a numeric value. 
#    (Or pick your own fruit name.)
prices["cherry"] = 0.5
prices

# b. Write the code for a loop that iterates over the stock dictionary and prints each key and value.
for key in stock:
    print(key, stock[key])

# c. Suppose that we have a list:
#    groceries = [‘apple’, ‘banana’, ‘pear’]
# Write the code that will sum the total number in stock of the items in the groceries list.
groceries = ["apple", "banana", "pear"]

# sum the total number of items in the grocery list that are in stock
sumStock = 0
for item in groceries:
    sumStock = sumStock + stock[item]
print("Total in stock items from grocery list: ", sumStock)    

# d. Write the code that can print out the total value in stock of all the items. 
#    This program can iterate over the stock dictionary and for each item multiply the number in 
#    stock times the price of that item in the prices dictionary. (This can include the items for 
#    ‘cherry’ or not, as you choose.)

stockValue = 0
for key in stock:
    stockValue = stockValue + prices[key]*stock[key]
print("Total in stock items in store: ${:.2f}".format(stockValue))    

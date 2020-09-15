# Week 2
# Class - Week 2
# Author: Joyce Woznica
# Class: IST 652
# 

#Your group will have 15 minutes to write a program that:
#     1. prompts a user for their name 
#     2. and then welcomes them. 
#     3. Then prompt them to enter a Celsius temperature, 
#     4. convert the temperature to Fahrenheit and 
#     5. print out:
#    a. their name, 
#    b. the temperature entered,
#    c. and the converted temperature.
#Consider checking for errors in what the user enters.

#Your group will report back with the code written and the results.
#
#formula for conversion:
#      fahren = (9/5 * cel) + 32
#
#Run the code 2 or 3 times to try different values

# Accept input of User's Name
userName = input("Enter Your Name: ")

# Welcome the User
print("Welcome, " + str(userName) + "!")

# Accept input of Celsius temperature
cTemp = input("Enter Celsius temperature: " )

# must check that this is numeric
# determine Fahrenheit
def test_temp(value):
    try:
        if value.isnumeric(): farh = (9/5 * float(value)) + 32
        else: farh = "Bad Temperature - Please enter a value between 0 and 100."
    except: 
        farh = "Bad Temperature"
    return farh

# convert to Fahrenheit
fTemp = test_temp(cTemp)

# print responses
print("Name: " + userName)
print("Celsius Temperature: " + cTemp)
print("Converted Fahrenheit Temperature: " + str(fTemp))

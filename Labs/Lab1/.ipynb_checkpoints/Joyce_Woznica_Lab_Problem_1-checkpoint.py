# Week 3
# Lab 1
# Author: Joyce Woznica
# Class: IST 652
# 

# For the NBAfile.py program, for each line, 
#   create a string using string formatting that puts the team, attendance, 
#   and ticket prices into a formatted string. Each line should look something like:
# ‘The attendance at Atlanta was 13993 and the ticket price was $20.06’

# Your program should then print these strings instead of the lines. 

# This program reads a file and prints the lines and creates a list of items on the line
# open the file for reading (in the same directory as the program)

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
        print('The attendance at ' + team + ' was '+ attendance + ' and the ticket price was $' + price + '.' )


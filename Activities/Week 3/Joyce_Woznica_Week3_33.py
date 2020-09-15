# Week 3
# Week 3 Activities - Dictionary (keys/values)
# Author: Joyce Woznica
# Class: IST 652
# 

# This program reads a file and prints the lines and creates a list of items on the line
# open the file for reading (in the same directory as the program)
filePath = '/Users/joycewoznica/Syracuse/IST652/Activities/Week 3/NBA-Attendance-1989.txt'
# open and read the file
nbaFile = open(filePath,'r')

# Create a list object with all the lines from the file
nbaList = []
for line in nbaFile:
     textline=line.strip()
     items = textline.split()
     nbaList.append(items)

# Get length for averages
totalTeams = len(nbaList)

# Create a list object for all the attendances in the file
attendances = []
for line in nbaList:
     attendances.append(int(line[1]))
# Sum all the Attendances
totalAtt = sum(attendances)
# Get average
avgAtt = totalAtt/totalTeams
# round to a whole number
print ('Average Attendance was {:.0f}'.format(avgAtt))

# Gather the total price for all tickets looping through List
team, att, price = nbaList[0]
# Blank list for Price
prices = []
for (team, att, price) in nbaList:
     prices.append(float(price))
avgPrice = sum(prices) / len(prices)
avgPrice = sum(prices) / totalTeams
# round to 2 decimal points
print("Average Ticket Price was ${:.2f}".format(avgPrice))

# Gather Highest Attendance and Ticket Price
maxAtt = max(attendances)
maxPrice = max(prices)

# Blank list for Teams
teams = []
for (team, att, price) in nbaList:
     teams.append(team)

# Max attendance by Team
maxTeamAtt=teams[attendances.index(maxAtt)]
maxTeamPrice = teams[prices.index(maxPrice)]
print ("Team with highest attendance was " + maxTeamAtt + " with attendance of ", maxAtt)
print ("Team with the highest price was " + maxTeamPrice + " with a high price of: ${:.2f}".format(maxPrice))


# 3.3 - Dictionaries
phonedict = {"Sam": "607-555-1212", "Judy": "860-555-1212", "Joe": "305-555-1212", "Gerald": "315-555-1212", "Jim": "281-555-1212"}
# print before sorting
phonedict

for key in sorted(phonedict):
    print (key, phonedict[key])
    
    
# 3.4 Sorting Lists
# Given a list of non-empty tuples, 

jTuple = [(1,7),(1,3),(3,4),(2,2)]

# write a sort expression that will sort in increasing order by the last element in each tuple.
sortedTuple = sorted(jTuple, key=lambda jTuple: jTuple[1])
sortedTuple

# Reading CSV Files

import csv
filePath = "/Users/joycewoznica/Syracuse/IST652/Activities/Week 3/states_data.csv"

# create new empty list
statesList = []

# loop through the file
with open(filePath, 'r') as csvfile:
    # the csv file reader returns a list of the csv items on each line
    stateReader = csv.reader(csvfile,  dialect='excel', delimiter='\t')

    # from each line, a list of row items, put each element in a dictionary
    #   with a key representing the data
    for line in stateReader:
      # skip lines without data, specific for each file to catch non-data lines
      if line[0] == '' or line[0].startswith('Data') or line[0].startswith('*'):
          continue
      else:
          # create a dictionary for each state
          state = {}
          # add each piece of data under a key representing that column data
          state['name'] = line[0]
          state['abbrev'] = line[1]
          state['code'] = line[2]
          state['area'] = int(line[3].replace(',',''))
          state['pop'] = int(line[4].replace(',',''))

          # add this state to the list
          statesList.append(state)
          
# close the file    
csvfile.close()


print ("Read", len(statesList), "states from the state data")

# print a few fields from all of the states read from the file
for state in statesList:
    print ('State:', state['name'], ' Abrv: ', state['abbrev'], ' Population: ', state['pop'])


# more
#import csv
filePath = "/Users/joycewoznica/Syracuse/IST652/Activities/Week 3/tv_life.csv"

# create new empty list
countryList = []

with open(filePath, 'r') as csvfile:
    # the csv file reader returns a list of the csv items on each line
    countryReader = csv.reader(csvfile,  dialect='excel', delimiter=',')

    # from each line, a list of row items, put each element in a dictionary
    #   with a key representing the data
    for line in countryReader:
      #skip lines without data, specific for each file to catch non-data lines
      if line[0] == '' or line[0].startswith('Televison') or line[0].startswith('SOURCE') \
              or line[0].startswith('Country'):
          continue
      else:
          try:
            # create a dictionary for each country
            country = {}
            # add each piece of data under a key representing that data
            country['name'] = line[0]
            country['life'] = line[1]
            country['people_tv'] = line[2]
            country['people_dr'] = line[3]
            country['femalelife'] = line[4]
            country['malelife'] = line[5]
    
            # add this countryto the list
            countryList.append(country)
          # catch errors in file formatting (number items per line)  and print an error message
          except IndexError:
            print ('Error: ', line)
            
# close file
csvfile.close()

print ("Read", len(countryList), " lines of country data")

# explore values of a numeric field
fieldname = 'life'
# collect the values in this list as numbers
numberList = []
for num, country in enumerate(countryList):
    try: 
        #print(num, country['name'])   
        numberList.append (float(country[fieldname]))
    except ValueError:
        print ('Number conversion error on value', country[fieldname], 'at line', num, 'Min and max not valid')

# report the average, max and min values and the first ones
maxval = max(numberList)
#print(numberList.index(maxval))
maxname = countryList[numberList.index(maxval)]['name']
minval = min(numberList)
#print(numberList.index(minval))
minname = countryList[numberList.index(minval)]['name']
avg = sum(numberList) / len(numberList)
print( 'Field', fieldname, '(First) Maximum', maxval, 'at', maxname)
print( 'Field', fieldname, '(First) Minimum', minval, 'at', minname)
print( 'Field',  'Average', avg)

# Consider the following two dictionairies:
stock = {"banana":6,"apple":0,"orange":32,"pear":15}
prices={"banana":4,"apple":2,"orange":1.5,"pear":3}

#    Show the expression that gets the value of the stock dictionary at the key "orange". Add another item to the dictionary ("cherry", 14).

oValue = stock["orange"]
oValue

#    Show a statement that adds an item to the stock dictionary called ‘cherry’ with some 
#    integer value 
stock["cherry"] = 14
stock

#    Write the code for a loop that iterates over the stock dictionary and prints each key and value.
for key in stock:
    print(key, stock[key])

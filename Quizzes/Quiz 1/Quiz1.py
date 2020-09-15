# Quiz 1

# Question 1
m = True
n = 3.14
q = "−7.2345907654"
print (type(m))
print(type(n))
print(type(q)) 

# Question 2
String1 = 'Monty Python'
String2 = "Monty Python"
String3 = 'Monty ' + 'Python' 

# Question 3
Students[]=0
Students[]=empty
Students = []
Students = ['']

# Question 4
Evennumbers = [2, 4, 6, 8, 10, 12, 14, 16, 18]
Temp = Evennumbers[1]+Evennumbers[3]
Evennumbers[1]
Evennumbers[3]
Evennumbers[7]
Temp

# Question 5
Suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
#What will be the value of Suitcase[1:] and Suitcase[:4], respectively? 
Suitcase[1:]
Suitcase[:4]

# Question 6
x = 5
if (x <= 0 and x < 0):
    print("Welcome to the world of logical operators")
else:
    print("Try Again")

if (x <= 0 or x > 5):
    print("Welcome to the world of logical operators")
else:
    print("Try Again")

if (x >= 0 or x < 0):
    print("Welcome to the world of logical operators")
else:
    print("Try Again")
    
if (x == 5 and x < 5):
    print("Welcome to the world of logical operators")
else:
    print("Try Again")
    
# Question 7
xlist = [1, 2, 3, 4]
for x in xlist:
     print(x + 1) 
     
# Question 8
nlist = [8, 92, 79, 55, 23, 17, 4, 45, 63, 9, 100]
threshold = input('Type Threshold: ')
if (max(nlist) > threshold):
     print('Great')
else:
     print('Not great') 
     
# Question 9
# Question 10

# Question 11
# Suppose that you have a list of strings named examples. 
# Write a Python loop that goes through the list and prints each string where the string length is 
# three or more and the first and last characters of the strings are the same.

examples = ['abab', 'xyz', 'aa', 'x', 'bcb']
examples = ['', 'x', 'xy', 'xyx', 'xx']
examples = ['aaa', 'be', 'abc', 'hello']

# Loop
for item in examples:
    if (len(item) >= 3 and item[-1] == item[0]):
        print(item)

# Question 12
# Reading and processing data in a file
# For this question, you are to write a program that reads the data in the file state_satscores_2004.txt. 
# Each line of this file has name of a state, mean Verbal SAT score, and mean Math SAT score.
filePath = "/Users/joycewoznica/Syracuse/IST652/Quizzes/Quiz 1/state_satscores_2004.txt"

statelist = []
vSATlist = []
mSATlist = []

# loop through each line
with open(filePath, 'r') as satFile:
    for satLine in satFile:
        # strip out newlines
        satLine = satLine.strip('\n')
        # split by tabs
        satVars = satLine.split('\t')
        # remove any empty items from list created
        satVars = list(filter(lambda x: x!= "", satVars))
        # assign variables to each item in list
        state, vSATm, mSATm = satVars
        # build lists of each of these so can do max at end
        statelist.append(state)
        vSATlist.append(vSATm)
        mSATlist.append(mSATm)

satFile.close()

# After reading the data,
# a. Print the state with the highest mean Verbal SAT score
# max Verbal SAT
vSATmax = max(vSATlist)
# find the index of this score and the matching state
stateName = statelist[vSATlist.index(vSATmax)]
print("State: " + stateName + " has the highest mean Verbal SAT score with a score of " + vSATmax + ".")

# b. Print each state that has a mean Math SAT score greater than 500
for item in mSATlist:
    if (int(item) > 500):
        i = mSATlist.index(item)
        print("State: " + statelist[i] + " has a mean Math SAT score greater than 500 with a score of " + item + "." )


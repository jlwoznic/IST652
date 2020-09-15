# Joyce Woznica
# Quiz 2

# Question 1
# this one is not a valid dictionary
d = (3,'three',5,'five')

d = {}
d = {3:'three',5:'five'}
d = {'3':'three','5':'five'} 

# Question 2
people = {'hugh':49,'kate':35,'lucy':24,'bob':36}

# this one is not correct
total = 0
for key in people:
     total += key 
     
total = 0
for x in people.values():
     total += x 
total

total = sum(people.values()) 
total

total = 0
for key in people:
     total += people[key] 
total

# Question 3
people = {'hugh':49,'kate':35,'lucy':24,'bob':36}
people['dan']

# since dan not a key - get a KeyError

# Question 4
peoplelist = [{'name':'bob','age':28},{'name':'dylan','age':43},{'name':'cat','age':17}]
for item in peoplelist:
    if item['age']>30:
        print(item['name']) 
# answer is dylan
          
# Question 5
def mystery(x):
    if x > 0:
        return −x
    else:
        return x 
      
# function doesn't work, so guessed at answer

# Question 6
import numpy as np
c = np.array([[2,4,6,8],[12,14,16,18],[22,24,26,28]])
print(c)
c.shape
# answer is (3,4)

# Question 7
import numpy as np
c = np.array([[2,4,6,8],[12,14,16,18],[22,24,26,28]])
# need to get just second row [12,14,15,18]

c[:,1]
c[1,:] # this is correct
c[2,:]
c[:,2]  

# Question 8
d = np.array([6,16,26])
# what to assign all values >10 to 0
d = 0
d[d<=10]=0
d[d>10]=0 # this is correct
d[d>10]=d

# Question 9
import datetime 
D1 = datetime.datetime(2017,2,22,9,30)
D2 = datetime.datetime(2017,2,23,10,45) 
# what can you do?
D1 < D2
D1 - D2
# Answer is all of the above

# Question 10
# dictionary
word_freq = {'the':58, 'people':6, 'beautiful':8, 'cats':13, 'finally':9, 
             'this': 19, 'class': 21, 'is': 101, 'almost': 1, 'over':4}
# write a function that takes the value and has a threshold number
def top_words(dxnry, threshold):
    new_array = []
    for key in dxnry:
        if dxnry[key] > threshold:
            new_array = np.append(key, new_array)
    return list(reversed(new_array));

# test the function
run_top = top_words(word_freq, 9)
run_top

run_top = top_words(word_freq, 15)
run_top

run_top = top_words(word_freq, 40)
run_top

# Question 11
import pandas as pd
import numpy as np
infile = '/Users/joycewoznica/Syracuse/IST652/Quizzes/Quiz2/Eur.pop.rev.csv'
popDF = pd.read_csv(infile)

# clean up the dataframe
# drop the first row - all empty
popDF = popDF.drop([0], axis=0)
# rename columns
popDF.columns
popDF.columns = ['Country', '1989', '1990', '1991', '1992', '1993', '1994', '1995']
# drop the first row again
popDF = popDF.drop([1], axis=0)
# drop last 3 rows
popDF = popDF[:-4]
# reindex by country
popDF.set_index(['Country'],inplace=True)

# 1. replace all NA data with 0
popDF = popDF.fillna(0)

# 2. Print each country that has more than 1,000,000 people in 1995
# convert to numeric for future use
popDF = popDF.astype(int)
countryNames = popDF[popDF['1995'] > 1000000].index
for country in countryNames:
    print ("Country: ", country, ".")
    
# 3. Print the average populuation in the UK over seven years
popUK = popDF.loc['United Kingdom', :]
meanUK = popUK.mean()
print('Average Population over Seven Years for the United Kingdom is {:.0f}'.format(meanUK))

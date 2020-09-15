# Week 7
# Joyce Woznica
# Working with JSON

# working with urllib
import urllib.request
import json

earthquake_url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"

response = urllib.request.urlopen(earthquake_url)

# unicode transformation format
json_string = response.read().decode('utf-8')

# start parsing this information
eq_parsed_json = json.loads(json_string)
type(eq_parsed_json)
eq_parsed_json.keys()
eq_parsed_json['metadata']
eq_parsed_json['type']

title = eq_parsed_json['metadata']['title']
title
quakelist = eq_parsed_json['features']
len(quakelist)

quake1 = quakelist[0]
quake1.keys()

# can keep going deeper here
print(json.dumps(quake1, indent = 2))

# Unicode

15

0xFF

0x7F

'\u0394'

"\U00000394"

"\N{GREEK CAPITAL LETTER DELTA}"

b'\xFFab'

type(b'ab')

type(b'\xFFab')

len(b'\xFFab')

u=chr(40960) + 'abcd' + chr(1972)

type(u)

u

print(u)

u.encode('ascii','ignore')

u.encode('ascii','replace')

u.encode('ascii', 'xmlcharrefreplace')

u.encode('ascii', 'backslashreplace')


# 7.4 Mongodb

import pymongo

from pymongo import MongoClient
client = MongoClient('locaalhost', 27017)

client.database_names()

db = client.peopledb
db.collection_names()

# Create a new collection or use an existing collection
peoplecoll = db.people
type(peoplecoll)

# list of dictionaries to be used as documents in the collection
peoplelist = [{ "name": "John Smith", "age": 30 }, 
              { "name": "Bo Bennett", "age": 23 }, 
              { "name": "Anna Jones", "age": 25 }]

# insert one document
peoplecoll.insert_one({ "name": "John Smith", "age": 30 })
# insert several documents
peoplecoll.insert_many(peoplelist[1: ])

docs = peoplecoll.find()
type(docs)
for doc in docs:
    print(doc)
    
morepeoplelist = [{ "name": "Britney Sykes", "age": 21 , 'position':'Guard'}, 
                  { "name": "Briana Day", "age": 21, 'position':'Center'}, 
                  { "name": "Alexis Peterson", "age": 21, 'position':'Guard' }, 
                  { "name": "Gabby Cooper", "age": 18, 'position':'Guard'}]

peoplecoll.insert(morepeoplelist)

docs = peoplecoll.find()
type(docs)
for doc in docs:
    print(doc)
    
# Query
peoplecoll.find_one()

result = peoplecoll.find_one({'name':'Anna Jones'})
print(result)

results = peoplecoll.find({'position':'Guard'})
for result in results:
    print(result)

# Exercise
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
client.database_names()

# people database
db = client.peopledb
db.collection_names()

# Create a new collection or use an existing collection
peoplecoll = db.people
type(peoplecoll)

peoplelist = [{ "name": "Britney Sykes", "age": 21 , 'position':'Guard'}, 
                  { "name": "Briana Day", "age": 19, 'position':'Center'}, 
                  { "name": "Alexis Peterson", "age": 21, 'position':'Guard' }, 
                  { "name": "Gabby Cooper", "age": 18, 'position':'Guard'}]

peoplecoll.insert_many(peoplelist)

docs = peoplecoll.find()
type(docs)
for doc in docs:
    print(doc)
    
# Query
results = peoplecoll.find({"age": {"$lt": 20}})
for result in results:
    print(result)

# drop the database if necessary (I made mistakes and had to do this)
peoplecoll.drop()

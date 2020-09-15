'''
    This main function retrieves documents from a file and writes them to a Mongo database collection,
        where each line of the file is a document represented as a json item
    It assumes that the Mongo DB server is running.
    Command line usage:
        python DB_from_file.py <DB name> <collection name> <filepath>
    Example:      python DB_from_file.py fbusers cdelta out/fb-delta-feed.txt 
        (where quotes may not be necessary)
'''


# This program contains functions to save and load from database collections in Mongo
#   They connect to mongod running on port 27017 on the localhost


import pymongo
import json
from bson.json_util import dumps


# This function either starts or adds to an existing database and collection in Mongo
# Parameters:  
#   data - this should be a list of json objects, where each will be a collection element
#      in the DB stored under a unique ID key created by Mongo
#   DBname - the name of the database, either new or existing
#   DBcollection - the name of the collection, either new or existing

def save_to_DB (DBname, DBcollection, data):
    # connect to database server and just let connection errors fail the program
    client = pymongo.MongoClient('localhost', 27017)
    # save the results in a database collection
    #   change names to lowercase because they are not case sensitive
    #   and remove special characters like hashtags and spaces (other special characters may also be forbidden)
    DBname = DBname.lower()
    DBname = DBname.replace('#', '')
    DBname = DBname.replace(' ', '')
    DBcollection = DBcollection.lower()
    DBcollection = DBcollection.replace('#', '')
    DBcollection = DBcollection.replace(' ', '')

    # use the DBname and collection, which will create if not existing
    db = client[DBname]
    collection = db[DBcollection]   
        
    # add the data to the database
    collection.insert_many(data)
    print("Saved", len(data), "documents to DB collection", DBname, DBcollection)


# This function gets data from an existing DB and collection
# Parameters:  
#   DBname and DBcollection- the name of the database and collection, either new or existing
# Result:
#   data - returns all the data in the collection as a list of JSON objects

def load_from_DB (DBname, DBcollection):
    # connect to database server and just let connection errors fail the program
    client = pymongo.MongoClient('localhost', 27017)
    # use the DBname and collection, which will create if not existing
    db = client[DBname]
    collection = db[DBcollection]    
        
    # get all the data from the collection as a cursor
    docs = collection.find()
    #  convert the cursor to a list
    docs_bson = list(docs)
    docs_json_str = [dumps(doc) for doc in docs_bson]
    docs_json = [json.loads(doc) for doc in docs_json_str]
    return docs_json



import json
import sys
from db_fn import save_to_DB

# use a main so can get command line arguments
if __name__ == '__main__':
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args or len(args) < 3:
        print('usage: python DB_from_file.py <DB name> <collection name> <filepath>')
        sys.exit(1)
    DBname = args[0]
    DBcollection = args[1]
    filename = args[2]  
    
    # get the data from the file
    fload = open(filename, encoding='utf-8')
    resultString = fload.read()
    # loads converts from a string back to a json structure
    doclist = json.loads(resultString)  
    print ("Read", len(doclist), "from file:", filename)

    # in case this was saved from a database, we delete the database id key _id, so that DB will assign unique key
    for doc in doclist:
        if '_id' in doc.keys():
            del doc['_id']
    
    # use the save and load functions in this program
    save_to_DB(DBname, DBcollection, doclist)


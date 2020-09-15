# MongoDB Activity
import urllib.request
import json
import pymongo
import datetime

# get the bbc rss feed of news stories and connect to it
earthquake_url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson"

try:
	response = urllib.request.urlopen(earthquake_url)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
	# the url request was successful - convert the response to a string
	json_string = response.read().decode('utf-8')

	# the json package loads() converts the string to python dictionaries and lists
	eq_json = json.loads(json_string)
	
	# from the json dictionary we get the title to print
	title = eq_json['metadata']['title']
	print('Collected data from', title)
	#  and we get the list of earthquakes
	quakelist = eq_json['features']

	# Connection to Mongo DB
	try:
	    client=pymongo.MongoClient('localhost', 27017)
	    print ("Connected successfully!!!")
	except pymongo.errors.ConnectionFailure as e:
	   print ("Could not connect to MongoDB: %s" % e )
	else:

		# use database named usgs or create it if not there already
		eqdb = client.usgs
		# create collection named earthquakes or create it if not there already
		quakecoll = eqdb.earthquakes
		# add all the earthquakes to the list
		quakecoll.insert_many(quakelist)
		print("Added", len(quakelist), "to earthquakes collection in usgs database")
		# close the database connection
		client.close()

# Added for Part B
# quakecoll is the earthquake collection
# I could not decipher the date format to properly convert it :(
quakes = quakecoll.find()

for quake in quakes:
    props = quake.get('properties')
    place = props.get('place')
    time = props.get('time')
    magnitude = props.get('mag')
    # convert time from its current format to get Date and time
    s = time / 1000.0
    newdatetime = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%m:%S.%f')
    print("Quake Location: ", place, ", Date/Time: ", newdatetime, ", Magnitude: ", magnitude)
    
# drop the database if necessary (I made mistakes and had to do this)
quakecoll.drop()

"""
This file cleans the armageddon collections and removes and lat/lon pairs that are not numbers
allowing us to create a spatial index and do distance queries.

*********IMPORTANT**********
This script only works with the modfied csvs and jsons in my repo!!
"""
import pymongo  # package for working with MongoDB

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
collections = [db["airports"], db["cities"], db["earthquakes"], 
    db["volcanos"], db["meteorites"], db["ufos"]  ]

#filters out bad data from the collections
for collection in collections:
    initialCount = 0
    count = 0
    finalCount = 0
    initialCount = collection.count()

    for obj in collection.find():
        mongo_id = obj["_id"]
        lat = obj["latitude"]
        lon = obj["longitude"]
        # Check if lat and lon are ints or floats
        lati = isinstance(lat, int)
        loni = isinstance(lon, int) 
        flat = isinstance(lat, float)
        flon = isinstance(lon, float)
        
        # If the lat lons ARE numbers, insert it
        if (lati or flat) and (flat or flon):
            collection.update_one({'_id':mongo_id}, {"$set": {"loc" : { "type": "Point", "coordinates": [ lon, lat ] }}}, upsert=False)
        else:
            print(f"Removing: {lat},{lon}")
            collection.remove({'_id':mongo_id})
            count += 1
            
    finalCount = initialCount - count        
    print(f"Initial count: {initialCount}")
    print(f"Count not inserted: {count}")
    print(f"Final count: {finalCount}")


"""
This file cleans the armageddon collections and removes and lat/lon pairs that are not numbers
allowing us to create a spatial index and do distance queries.

*********IMPORTANT**********
This script only works with the modfied csvs and jsons in my repo!!
"""
import pymongo  # package for working with MongoDB

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
collection = db["plane_crashes"]



initialCount = 0
badCoordsCount = 0
finalCount = 0
initialCount = collection.count()
fatCount = 0

for obj in collection.find():
    mongo_id = obj["_id"]
    lat = obj["Latitude"]
    lon = obj["Longitude"]
    fat = obj["TotalFatalInjuries"]
    #changes fatality string to int
    collection.update_one({'_id':mongo_id}, {"$set": {"TotalFatalInjuries": int(fat)}}, upsert=False)

    if (lat == "  ") or (lon == "  ") or (lat == None) or (lon == None):
        badCoordsCount +=1
        collection.delete_one({'_id':mongo_id})
    else:
        fLat = float(lat)
        fLon = float(lon)
        #Changes the strings to floats for lat and lon
        collection.update_one({'_id':mongo_id}, {"$set": {"Latitude": fLat}}, upsert=False)
        collection.update_one({'_id':mongo_id}, {"$set": {"Longitude": fLon}}, upsert=False)
        collection.update_one({'_id':mongo_id}, {"$set": {"loc" : { "type": "Point", "coordinates": [ fLon, fLat ] }}}, upsert=False)
    if (fat == "  ") or (fat == None):
        fatCount += 1
        collection.delete_one({'_id':mongo_id})

        
finalCount = initialCount - badCoordsCount
print(f"Initial count: {initialCount}")
print(f"Unusable coordinates not inserted: {badCoordsCount}")
print(f"Number of usable documents: {finalCount}")


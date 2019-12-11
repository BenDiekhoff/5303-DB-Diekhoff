"""
Queries my collections to determine which city has the most meteor strikes.
"""

import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo
from bson.son import SON

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
meteors = db["volcanos"]
cities = db["cities"]

radius = 25000 #25 kilometers

query = {   
   "loc" : {
        "$geoWithin" : {
            "$centerSphere" : [db.cities["loc"], radius ]
        }
    }
}

#see if every volcano is inside city limits
for volcano in db.volcanos.find(query)



https://github.com/rugbyprof/5303-Adv-Database/tree/master/Lectures/L03
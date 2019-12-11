import numpy as np 
import pandas as pd
import plotly
#import plotly.plotly as py
#import plotly.offline as offline
import plotly.graph_objects as go
import pymongo


# declare my Database and its collections. I make collections a list
# because my program will loop through each one, opening each map in a new 
# browser tab.
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
collections = [db["airports"], db["earthquakes"], db["ufos"]]
token = open("mapbox_token.txt").read()

#Marker color needs to change with the collection being mapped
color = ["green", "orange", "blue"]
colorIndex = 0

lat =[]
lon = []

for collection in collections:
    for obj in collection.find():
        lat = obj["latitude"]
        lon = obj["longitude"]
    fig = go.Figure(go.Scattermapbox(
        lat = lat,
        lon = lon,
        mode = 'markers',
        marker=go.scattermapbox.Marker(size=9, color = color[colorIndex]),
    ))



    fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=38.92,
            lon=-77.07
        ),
        pitch=0,
        zoom=10
    ),
)

fig.show()
colorIndex += 1
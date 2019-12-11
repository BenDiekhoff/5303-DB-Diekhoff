"""
Plots the volcano and earthquake collection in the same tab but with 
different colors.
"""

import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
collections = [db["earthquakes"], db["volcanos"]]

# I will provide my token on request
token = token = open(r"mapbox_token.txt").read()

EQlat = []
EQlon = []
Vlat = []
Vlon = []

for obj in db["earthquakes"].find():
    EQlat.append(obj["latitude"],)
    EQlon.append(obj["longitude"])

for obj in db["volcanos"].find():
    Vlat.append(obj["latitude"],)
    Vlon.append(obj["longitude"])

fig = go.Figure()

fig.add_trace(
    go.Scattermapbox(
        lat = EQlat,
        lon = EQlon,
        mode = 'markers',
        marker= go.scattermapbox.Marker(size=9, color = "orange"), name = "Earthquake"
))
fig.add_trace(
    go.Scattermapbox(
        lat = Vlat,
        lon = Vlon,
        mode = 'markers',
        marker=go.scattermapbox.Marker(size=9, color = "yellow"), name = "Volcano"
))


fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=33.930828,
            lon=-98.484879
        ),
        pitch=0,
        zoom=3
    ),
)


plotly.offline.plot(fig, filename='EarthquakesAndVolcanos.html')

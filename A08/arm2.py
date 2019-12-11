#!/usr/local/bin/python3

import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
token = open(r"mapbox_token.txt").read()
volc = db["volcanos"]

volclist = []
lats = []
lons = []
for obj in volc.find():
    volclist.append(db["volcanos"].find().sort([("PEI", -1)]))
    lats.append(obj["latitude"])
    lons.append(obj["longitude"])
fig = go.Figure()

fig.add_trace(go.Scattermapbox(
                                    lat = lats,
                                    lon = lons,
                                    mode = "markers",   
                                    marker = {"size":[30, 30, 30],
                                    "color":["Red", "Orange", "Yellow"]}
                                    )
                                )
fig.add_trace(go.Scattermapbox(
                                    lat = lats,
                                    lon = lons,
                                    mode = "markers",   
                                    marker = dict(size =15, symbol = "volcano")
                                    )
                                )

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
        ))

fig.show()
plotly.offline.plot(fig, filename='volc.html')
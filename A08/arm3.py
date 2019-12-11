import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
token = open(r"mapbox_token.txt").read()
crash = db["plane_crashes"]
lats = []
lons = []
crash300lat = []
crash200lat = []
crash100lat = []
crashOtherlat = []
crash300lon = []
crash200lon = []
crash100lon = []
crashOtherlon = []

crashArray = [0, 0, 0 ,0]
# crashlist = []
# color = ["red", "orange", "yellow", "blue"]

for obj in crash.find():
    #crashlist.append(db["plane_crashes"].find().sort([("TotalFatalInjuries", -1)]))
    lats.append(obj["Latitude"])
    lons.append(obj["Longitude"])
    if (obj["TotalFatalInjuries"] > 300):
        #crashArray[0] += 1
        crash300lat.append(obj["Latitude"])
        crash300lon.append(obj["Longitude"])
    elif (obj["TotalFatalInjuries"] > 200):
        #crashArray[1] += 1
        crash200lat.append(obj["Latitude"])
        crash200lon.append(obj["Longitude"])
    elif (obj["TotalFatalInjuries"] > 100):
        #crashArray[2] += 1
        crash100lat.append(obj["Latitude"])
        crash100lon.append(obj["Longitude"])
    else:
        #crashArray[3] += 1
        crashOtherlat.append(obj["Latitude"])
        crashOtherlon.append(obj["Longitude"])

#print(crashArray[0])

fig = go.Figure()

fig.add_trace(go.Scattermapbox(
                                    lat = crash300lat,
                                    lon = crash300lon,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "red"}
                                    )
                                )

fig.add_trace(go.Scattermapbox(
                                    lat = crash200lat,
                                    lon = crash200lon,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "orange"}
                                    )
                                )                                

fig.add_trace(go.Scattermapbox(
                                    lat = crash100lat,
                                    lon = crash100lon,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "yellow"}
                                    )
                                )

fig.add_trace(go.Scattermapbox(
                                    lat = crashOtherlat,
                                    lon = crashOtherlon,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "blue"}
                                    )
                                )      

## I don't think an airplane symbol exists                                                          
# fig.add_trace(go.Scattermapbox(
#                                     lat = lats,
#                                     lon = lons,
#                                     mode = "markers",   
#                                     marker = dict(size =15, symbol = "plane")
#                                     )
#                                 )

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
            zoom=1
        ))

#fig.show()
plotly.offline.plot(fig, filename='plane_crash.html')
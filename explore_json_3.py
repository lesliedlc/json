import json

in_file = open("eq_data_30_day_m1.json", "r")

out_file = open("readable_eq_data.json","w")

eq_data = json.load(in_file) #take native json file and load it into python variable 

#json.dump(eq_data, out_file,indent = 4) #dump contents into the file

list_of_eqs = eq_data["features"]

print(type(list_of_eqs)) #type

print(len(list_of_eqs)) #how many eqs are in the list

mags,lons,lats,hover_text = [],[],[],[]

for eq in list_of_eqs:
    mag = eq["properties"]['mag']
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    title = eq["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)


print("mag",mags[:10])
print("lon",lons[:10])
print("lat",lats[:10])

#import plotly

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_text,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]

my_layout = Layout(title="Global Earthquakes")

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename = "global_earthquake.html")
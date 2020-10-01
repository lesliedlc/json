import json

in_file = open("US_fires_9_14.json", "r")
out_file = open("readable_US2_data.json","w")

us2_data = json.load(in_file)
json.dump(us2_data, out_file,indent = 4) #dump contents into the file

fire_list_1 = us2_data[:]

print(type(fire_list_1)) #type

print(len(fire_list_1)) #how many

brightness,lons,lats = [],[],[]

for F in fire_list_1:
    brg = F["brightness"]
    lon = F["longitude"]
    lat = F["latitude"]
    if brg > 450:
        brightness.append(brg)
        lons.append(lon)
        lats.append(lat)

print("Brightness:",brightness[:10])
print("Longitude",lons[:10])
print("Latitude",lats[:10])

#import plotly
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[brg/50 for brg in brightness],
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename = "US_fires_9_14-20.html")
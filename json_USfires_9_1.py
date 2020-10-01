import json

in_file = open("US_fires_9_1.json", "r") #imports the raw json file, reads
out_file = open("readable_US1_data.json","w") #Readable json file, writes

us1_data = json.load(in_file) #loads the raw json file 
json.dump(us1_data, out_file,indent = 4) #dump contents into the file

fire_list = us1_data[:] #creates a list 

print(type(fire_list)) #type

print(len(fire_list)) #how many

brightness,lons,lats = [],[],[] #new lists

for F in fire_list: #for loop to collect the brightness, lat, lon data 
    brg = F["brightness"]
    lon = F["longitude"]
    lat = F["latitude"]
    if brg > 450:
        brightness.append(brg)
        lons.append(lon)
        lats.append(lat)

#prints out the data collected for the first 10 indexes
print("Brightness:",brightness[:10])
print("Longitude",lons[:10])
print("Latitude",lats[:10])

#import plotly
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#scattergeo plot parameters in dictionary
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

my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename = "US_fires_9_1-13.html") #offline html of map
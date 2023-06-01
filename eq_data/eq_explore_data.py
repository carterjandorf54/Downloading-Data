from pathlib import Path
import json

# Import plotly 
import plotly.express as px

# Read data as a string and convert it to a Python Object
data = r"C:\Users\carte\OneDrive\Desktop\Python\Downloading Data\eq_data\eq_data_30_day_m1.geojson"
path = Path(data)
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# Get the information we want out of the json dump
mags, lats, longs, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mag = eq_dict['properties']['mag']
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# Create a plot of the data
title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=longs, size=mags, title=title, color=mags,
                     color_continuous_scale="Viridis",
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
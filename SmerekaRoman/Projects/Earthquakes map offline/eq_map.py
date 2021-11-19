import json
from plotly.graph_objs import scattergeo, layout
from plotly import offline


#досліджуємо структуру данних

filename = r'C:\Users\super\Desktop\python_work\Lv-639.pythonCore\SmerekaRoman\Earthquakes map offline\significant_month.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readble_file = r'C:\Users\super\Desktop\python_work\Lv-639.pythonCore\SmerekaRoman\Earthquakes map offline\readble_eq_data.json'
with open(readble_file, 'w') as f:
    json.dump(all_eq_data, f, indent = 4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#наносимо на карту світу землетруси

data_set = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
        }
}]

#my_layout_1 = layout(title = 'Global Earthquakes')

fig = {'data': data_set, 'layout': {"title": {"text": 'Significant Earthquakes, Past Month'}}}
offline.plot(fig, filename = 'global_earthquakes.html')


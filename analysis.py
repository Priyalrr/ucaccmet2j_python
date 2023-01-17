import json
with open('precipitation.json') as file:
  measurements_dict=json.load(file)

for station_line in measurements_dict:
    station=station_line["station"]
    value=station_line["value"]
    date=station_line["date"]
    split_date=split.date
    if station=="GHCND:US1WAKG0038":
        seattle_values=value
        print(seattle_values)

list_of_months=[0,0,0,0,0,0,0,0,0,0,0,0]

seattle_value=0
for station_line in measurements_dict:
    split_date=
    if seattle_value is not in list_of_months:
        seattle_value+=seattle_values
    else seattle_value=seattle_values


     





    

        

    


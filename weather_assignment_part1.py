import json
with open('precipitation.json') as file:
  measurements_dict=json.load(file)

total_monthly_precipitation=[0,0,0,0,0,0,0,0,0,0,0,0] #a list where each element corresponds to the total precipitation value for each month

for station_line in measurements_dict:
    station=station_line["station"]
    value=station_line["value"]
    date=station_line["date"]
    if station=="GHCND:US1WAKG0038":
        seattle_value=value
        split_date=date.split('-') #isolating the month from the whole date
        month=split_date[1]
        month=int(month)
        total_monthly_precipitation[month-1]+=seattle_value  #the index of the list corresponds to the (month-1)
        print(total_monthly_precipitation)    
    
import json
results={
    "Seattle":{
        "State": "WA",
        "Station": "GHCND:US1WAKG0038",
        "total_monthly_precipitation": total_monthly_precipitation
        }
    }

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)

        








 


     





    

        

    


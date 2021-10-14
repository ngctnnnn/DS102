import requests
import json

# api = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/700000?unitGroup=metric&key="
lat = '10.762622'
long = '106.660172'
api = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + lat + ',' + long + '?key=' 
api_key = "KC7SPM46W49HDFWL3PX4AP3PX"

response = requests.get(api + api_key)
df_json = response.json()
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(df_json, f, ensure_ascii=False, indent=4)


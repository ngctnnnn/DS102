import requests
import json
response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/700000/?key=KC7SPM46W49HDFWL3PX4AP3PX')
df_json = response.json()
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(df_json, f, ensure_ascii=False, indent=4)


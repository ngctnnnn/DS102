import requests
import json
import pandas as pd
from constant import api_key
"""
feature=["Name",
         "Date time",
         "Maximum Temperature",
         "Minimum Temperature",	
         "Temperature",	
         "Wind Chill", 
         "Heat Index",
         "Precipitation",
         "Snow",	
         "Snow Depth",
         "Wind Speed",
         "Wind Direction",
         "Wind Gust",
         "Visibility",
         "Cloud Cover",
         "Relative Humidity",
         "Conditions"]
"""

def main(api, api_key):
    response = requests.get(api + api_key)
    df_json = response.json()
    with open('data/weather.json', 'w', encoding='utf-8') as f:
        json.dump(df_json, f, ensure_ascii=False, indent=4)


if __name__=='__main__':    
    df = pd.read_csv('data/GLC.csv')

    """ Get latitude and longitude to scrape api """
    latitude, longitude, date, time = [], [], [], []
    for idx in range(len(df)):
        latitude.append(str(df['latitude'][idx]))
        longitude.append(str(df['longitude'][idx]))
        date.append(str(df['event_date'][idx][:10]))
        time.append(str(df['event_date'][idx][11:]))

    
    # """ Scrape API """
    for i in range(1):
        lat, long = latitude[i], longitude[i]
        dt = date[i]
        api = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + lat + ',' + long + '/' + dt + '?key='   
        main(api, api_key)

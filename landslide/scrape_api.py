import requests
import json
import pandas as pd
from tqdm import tqdm
from constant import api_key, feature

""" Create a checkpoint after running"""
checkpoint = 10899 


def main(api, api_key, feature):
    response = requests.get(api + api_key + feature)
    df_json = response.json()
    with open('data/weather.json', 'a', encoding='utf-8') as f:
        json.dump(df_json, f, ensure_ascii=False, indent=4)
        f.write('\n')


if __name__=='__main__':    
    df = pd.read_csv('data/GLC.csv')

    backlink = '&include=obs%2Cfcst%2Cstats%2Calerts%2Ccurrent%2Chistfcst&elements='
    for idx in range(len(feature) - 1):
        backlink += feature[idx]+','
    backlink += feature[-1]

    """ Get latitude and longitude to scrape api """
    latitude, longitude, date, time = [], [], [], []
    for idx in range(len(df)):
        latitude.append(str(df['latitude'][idx]))
        longitude.append(str(df['longitude'][idx]))
        date.append(str(df['event_date'][idx][:10]))
        time.append(str(df['event_date'][idx][11:]))

    
    """ Scrape API """
    for i in tqdm(range(checkpoint + 1, len(df))):
        lat, long = latitude[i], longitude[i]
        dt = date[i]
        api = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + lat + ',' + long + '/' + dt + '?key='   
        main(api, api_key, backlink)

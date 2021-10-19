import json 
import numpy as np 
import pandas as pd 

def push_csv(direct_csv='./data/weather.csv', direct_json='./data/tmp_weather.json'): 
    file_json_tmp_weather = open('./data/tmp_weather.json', ) 
    data = json.load(file_json_tmp_weather) 
    prefix_row = [] 
    rows = []
    for primary_key in data:  
        if primary_key != 'days' and primary_key != 'stations':  
            prefix_row.append(data[primary_key])
            pass

        if primary_key == 'days': 
            for key in data['days'][0]: 
                if key != 'stations' and key != 'normal':  
                    prefix_row.append(data['days'][0][key])
            pass

        if primary_key == 'stations': 
            pass
        #     for key_station in data['stations']: 
        #         row = prefix_row.copy()
        #         row.append(key_station)

        #         for key in data['stations'][key_station]: 
        #             row.append(data['stations'][key_station][key])

        #         rows.append(row)
        #     pass   
    rows.append(prefix_row) 
    return rows  


def make_name_column(): 
    name = [ 
        "queryCost","latitude","longitude","resolvedAddress","address","timezone","tzoffset",
        "feelslikemax","feelslikemin","feelslike","dew","humidity","precip","precipprob","precipcover",
        "preciptype","snow","snowdepth","windgust","windspeed","winddir","pressure","cloudcover",
        "visibility","solarradiation","solarenergy","uvindex","moonphase","conditions","description","icon" 
    ]
    return name

if __name__=='__main__':   

    file_json_weather = open('./data/weather.json', 'r') 
    new_json = []
    table = []  

    table.append(make_name_column())
 

    for line_json_weather in file_json_weather:  
        if len(line_json_weather) > 0: 
            new_json.append(line_json_weather)

            if line_json_weather[0] == '}':
                # Open file temp to write each json 
                file_json_tmp = open('./data/tmp_weather.json', 'w')
                
                for i in new_json: 
                    file_json_tmp.write(i) 

                file_json_tmp.close()  

                # Renew json -> Read next json
                new_json = [] 
                
                # Push to csv
                row_csv = push_csv()
                
                for row in row_csv: 
                    table.append(row)
 

    pd.DataFrame(table).to_csv("./data/weather.csv", header=None, index=False) 
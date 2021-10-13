import json 
import numpy 
import pandas 

js = open('data.json',) 
data = json.load(js) 
name_column = [] 
final_result = [] 

for name in data: 
    if name != 'alerts' and name != 'stations' and name != 'currentConditions': 
        name_column.append(name)  


for day in data['days']: 
    for name in day: 
        if name != 'hours': 
            name_column.append(name)


    for hour in day['hours']: 
        for name in hour: 
            name_column.append(name)
        break

    break

final_result.append(name_column)

for day in data['days']:
    data_top = [] 
    data_top.append(data['queryCost'])
    data_top.append(data['latitude'])
    data_top.append(data['longitude'])
    data_top.append(data['resolvedAddress'])
    data_top.append(data['address'])
    data_top.append(data['timezone'])
    data_top.append(data['tzoffset'])
    data_top.append(data['description'])
    for i in day: 
        if i != 'hours':
            data_top.append(day[i])

    for hour in day['hours']: 
        data_bot = []
        for i in hour: 
            data_bot.append(hour[i])
    
        merge = data_top + data_bot
        final_result.append(merge)

pandas.DataFrame(final_result).to_csv("data_csv.csv", header=None) 
if __name__=='__main__':   

    file_json_weather = open('./data/weather.json', 'r') 
    new_json = [] 
    cnt = 0 
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
                
                cnt += 1
                if cnt == 2: 
                    break
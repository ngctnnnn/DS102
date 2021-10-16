import requests
import json
import matplotlib.pyplot as plt

api_key = 'k_j6kmyx2w'
lang = 'en'

""" Requests to get movie via name (and year) """
def SearchMovie(lang, api_key, query_name) -> dict:
    """
    Args: 
    lang -- results language
    api_key
    query_name -- name of the movie to query
    
    Returns:
    description -- movie release year
    id -- movie id
    image -- poster
    resultType -- type of result
    title -- movie title
    """
    url = 'https://imdb-api.com/' + lang + '/API/SearchMovie/' + api_key + '/' + query_name
    print(url)
    response = requests.get(url)
    df_json = response.json()
    return df_json 

def SearchSeries(lang, api_key, query_name) -> dict:
    url = 'https://imdb-api.com/' + lang + '/API/SearchSeries/' + api_key + '/' + query_name
    print(url)
    response = requests.get(url)
    df_json = response.json()
    return df_json  

def Top250Movies(lang, api_key) -> dict:
    """
    Get top 250 Movies on IMDB
    """
    url = "https://imdb-api.com/" + lang + "/API/Top250Movies/" + api_key
    response = requests.get(url)
    df_json = response.json()
    with open('data/top250movies.json', 'a', encoding='utf-8') as f:
        json.dump(df_json, f, ensure_ascii=False, indent=4)
        f.write('\n')
    return df_json

def main():
    # output = SearchMovie(lang, api_key, "minions")
    # output = SearchSeries(lang, api_key, "big bang theory") 
    # output = Top250Movies(lang, api_key)
    
if __name__ == '__main__':
    main()
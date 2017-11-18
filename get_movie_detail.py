import requests
import pprint

MAIN_URL = 'https://api.themoviedb.org/3/'
API_KEY = 'bdf7f7fc2775f4fc1bf8001c1d6e1ad0'

def get_url(op='search', movie_id=None):    
    if op == 'search':
        return MAIN_URL + 'search/movie?api_key=' + API_KEY 
    elif op == 'detail':
        return MAIN_URL + 'movie/' + str(movie_id) + '?api_key=' + API_KEY

def search_movie(movie_title):
    response = requests.get(url=get_url(), params={'query': movie_title})
    # pprint.pprint(response.json())
    return response.json()

def get_movie_details(movie_id):
    response = requests.get(url=get_url(op='detail', movie_id=movie_id))
    # pprint.pprint(response.json())
    return response.json()


search_movie('Harry Potter')

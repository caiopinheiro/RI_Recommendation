import get_movie_detail
from tornado import ioloop, httpclient
import pprint
import urllib
import json
from functools import partial

MOVIE_DAT_ID = 0
MOVIE_DAT_TITLE = 1
MOVIE_DAT_GENRES = 2

# movie_dat_stream = open('ml-1m/movies.dat', 'r')
# movie_out_stream = open('processed/movies.dat', 'w+')

# for line in movie_dat_stream.readlines():
#     items = line.split('::')
#     items[MOVIE_DAT_GENRES] = items[MOVIE_DAT_GENRES].strip()

#     title = items[MOVIE_DAT_TITLE]
#     old_title = title
#     title = title.split('(')[0]

#     print('Current Title: ' + title + ' from splitted ' + old_title)
#     json = get_movie_detail.search_movie(title)

#     movie = None
#     for element in json['results']:
#         if element['original_title'].lower().strip() == title.lower().strip():
#             movie = element
#             break

#     if movie:
#         items.append(movie['overview'] + '\n')

#     # print('::'.join(items))
#     movie_out_stream.write('::'.join(items))
#     print()
#     print()

movies_dict = {}
i = 0
def handle_request(url, response):
    global i
    pprint.pprint(response.code)

    if response.code == 200:
        i -= 1
        json_response = json.loads(response.body)
        movie = None
        items = None
        global movies_dict
        for element in json_response['results']:
            if element['original_title'].lower().strip() in movies_dict:
                movie = element
                items = movies_dict[element['original_title'].lower().strip()]
                break
        
        # print(items)
        if movie != None:
            items.append(movie['overview'] + '\n')
            movie_out_stream.write('::'.join(items))
    else:
        return http_client.fetch(url, partial(handle_request, url.strip()), method='GET')

    print()

    if i == 0:
        ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()
movie_dat_stream = open('ml-1m/movies.dat', 'r')
movie_out_stream = open('processed/movies.dat', 'w+')

for line in movie_dat_stream.readlines():
    items = line.split('::')
    items[MOVIE_DAT_GENRES] = items[MOVIE_DAT_GENRES].strip()

    title = items[MOVIE_DAT_TITLE].split('(')[0].lower().strip()

    movies_dict[title] = items
movie_dat_stream.close()

for element in movies_dict.items():
    url = get_movie_detail.get_url() + '&' + urllib.parse.urlencode({'query': element[0]})

    i += 1
    http_client.fetch(url.strip(), partial(handle_request, url.strip()), method='GET')

ioloop.IOLoop.instance().start()

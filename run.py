import requests
import sys
from bs4 import BeautifulSoup
import re
import os

# Map of artist name to number of movies they are in by decade (2000, 2010, 1920, 1930,.....1990)
maps = [{} for i in range(0,10)]
if not os.path.exists('output'):
    os.makedirs('output')
os.chdir('output')

def parse_request(url, artists):
    response = requests.get(url)
    url = re.search("(?P<url>https?://[^\s]+)", response.text).group("url")
    url = url[:url.index('"')]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup2 = BeautifulSoup(str(soup.find_all("th", string="Music by")[0].parent.td), 'html.parser')
    for name in soup2.find_all("a"):
        artists.append(name.string)

failed = 0
with open('../movies.txt','r') as fh, open('movies_processed.csv', 'w') as out_file:
    out_file.write('Movie, Artist')
    for line in fh:
        out_file.write('\n')
        search = line.strip()
        out_file.write(search + ', ')
        print(line, end='')
        year = 0
        artists = []

        try:
            year = int(search[search.rindex(' ')+1:])
            search = search.replace(' ', '%20')
            search = search.replace('\t', '%20')  
            url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + search + '&namespace=0&limit=10&suggest=true'
            parse_request(url, artists)
        except Exception as e:
            try:
                search = search[:search.rindex('%20')]
                url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + search + '&namespace=0&limit=10&suggest=true'
                parse_request(url, artists)
            except Exception as e:
                try:
                    search = search + "%20film"
                    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + search + '&namespace=0&limit=10&suggest=true'
                    parse_request(url, artists)
                except Exception as e:
                    # print('FAIL: ' + str(e))
                    # failed += 1
                    print()
                    continue
        
        # Add to artists count for that decade
        index = (year // 10) % 10
        for artist in artists:
            out_file.write(artist + '|')
            print(artist)
            maps[index][artist] = maps[index].get(artist, 0) + 1
        print()
# print('Num Failed: ' + str(failed))
            
# Make csv's for each map by decade
# print(maps)
for i in range(0, len(maps)):
    if(len(maps[i]) == 0):
        continue
        
    year = 1900 + 10 * i
    if(i < 2):
        # Year in 2000s not 1900s so add 100 to year
        year += 100
    filename = 'artist_to_num_movies_' + str(year) + '.csv'

    with open(filename, 'w') as out:
        out.write('Artist,# Of Movies They Wrote Songs For.\n')
        for artist in maps[i]:
            out.write(artist + ', ' + str(maps[i][artist]) + '\n')
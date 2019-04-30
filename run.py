import requests
import sys
from bs4 import BeautifulSoup
import re

failed = 0
with open('movies.txt','r') as fh, open('movies_processed.csv', 'w') as out_file:
    for line in fh:
        try:
            out_file.write('\n')
            search = line.strip()
            out_file.write(search + ', ')
            print(line, end='')
            search = search.replace(' ', '%20')
            search = search.replace('\t', '%20')
            url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + search + '&namespace=0&limit=10&suggest=true'

            response = requests.get(url)

            url = re.search("(?P<url>https?://[^\s]+)", response.text).group("url")
            url = url[:url.index('"')]

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            soup2 = BeautifulSoup(str(soup.find_all("th", string="Music by")[0].parent.td), 'html.parser')
            for name in soup2.find_all("a"):
                out_file.write(name.string + '|')
                print(name.string)
        except Exception as e:
            try:
                search = search[:search.rindex('%20')]
                url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + search + '&namespace=0&limit=10&suggest=true'

                response = requests.get(url)

                url = re.search("(?P<url>https?://[^\s]+)", response.text).group("url")
                url = url[:url.index('"')]

                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                soup2 = BeautifulSoup(str(soup.find_all("th", string="Music by")[0].parent.td), 'html.parser')
                for name in soup2.find_all("a"):
                    out_file.write(name.string + '|')
                    print(name.string)
            except Exception as e:
                try:
                    search = search + "%20film"
                    url = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search=' + search + '&namespace=0&limit=10&suggest=true'

                    response = requests.get(url)

                    url = re.search("(?P<url>https?://[^\s]+)", response.text).group("url")
                    url = url[:url.index('"')]

                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    soup2 = BeautifulSoup(str(soup.find_all("th", string="Music by")[0].parent.td), 'html.parser')
                    for name in soup2.find_all("a"):
                        out_file.write(name.string + '|')
                        print(name.string)
                except Exception as e:
                    # print('FAIL: ' + str(e))
                    # failed += 1
                    pass
            


# print('Num Failed: ' + str(failed))
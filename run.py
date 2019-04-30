import requests
import sys
from bs4 import BeautifulSoup

response = requests.get(sys.argv[1])
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(str(soup.find_all("th", string="Music by")[0].parent.td), 'html.parser')
for name in soup2.find_all("a"):
    print(name.string)
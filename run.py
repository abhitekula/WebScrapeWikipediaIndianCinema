import requests
import sys
from bs4 import BeautifulSoup

response = requests.get(sys.argv[1])
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find_all("th", string="Music by")[0].parent.td.a.string)
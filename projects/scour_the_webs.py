import requests
from bs4 import BeautifulSoup

r = requests.get('http://cdgriffith.com')

soup = BeautifulSoup(r.text, 'html.parser')
links = []
for link in soup.find_all('a'):
    print(link.get('href'))

    links.append(link.get('href'))

print(links)
with open('Outputttt.txt', "w") as f:
    for l in links:
        f.write(l)





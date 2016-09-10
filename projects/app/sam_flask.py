import requests
from bs4 import BeautifulSoup




def find_text(web_page):
    r = requests.get(str(web_page))
    soup = BeautifulSoup(r.text, "html.parser")
    text = []
    for text in soup.find_all('text', 'html.parser'):
        print(text.get('href')

find_text('http://cdgriffith.com')



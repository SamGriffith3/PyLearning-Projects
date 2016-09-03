import requests
from bs4 import BeautifulSoup


def scour_the_webs(web_page, output="output.txt"):  # set web_page = (your web page), output.txt set to default

    r = requests.get(web_page)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        print(link.get('href'))
        if link.get('href').startswith("http"):
            links.append(link.get('href'))

    print(links)
    with open(output, "w") as f:
        for l in links:
            f.write(l + '\n')





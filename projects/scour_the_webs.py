import requests
from bs4 import BeautifulSoup


def scour_the_links(web_page, output="output.txt"):  # set web_page = (your web page), output.txt set to default

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


def scour_the_html(web_page, output="text_output.txt"):
    r = requests.get(web_page)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = []
    text.append(soup.get_text)
    print(soup.get_text)

    print(text)
    with open(output, "w") as f:
        for t in text:
            f.write(str(t))


web_page = str(input("Which website? : "))
scour_the_links(web_page)
scour_the_html(web_page)




import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

import json


r = requests.get('http://cdgriffith.com')  #


soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))






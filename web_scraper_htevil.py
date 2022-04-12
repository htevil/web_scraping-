import requests

from bs4 import BeautifulSoup

page = requests.get('https://github.com/htevil/web_scraping-')

soup = BeautifulSoup (page.content, 'html.parser')

print(soup.find_all('a'))
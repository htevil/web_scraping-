from os import link
import requests

from bs4 import BeautifulSoup

url = input('Enter the url of web site :')
#url = 'https://www.amazon.in/'
lis = []

class recon:
    def getall_link (self,url):
        self.url = url
        page= requests.get(url)
        soup = BeautifulSoup (page.content, 'html.parser')
        #print(soup.prettify)
        #print( soup.find_all('a', href = True))
        for link in  soup.find_all('a', href = True):
            lis.append(link['href'])
        print(lis)

r = recon()
r.getall_link(url)



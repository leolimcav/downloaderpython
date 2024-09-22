import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# url = "https://myrient.erista.me/files/Redump/Microsoft%20-%20Xbox%20360/"

class Item:
    def __init__(self, name: str, link: str, size: str):
        self.name = name
        self.link = link
        self.size = size
        
    def print(self) -> str:
       return f'''Name: {self.name}\n     Link: {self.link}\n     Size: {self.size}\n'''

class Crawler:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def query(self, text: str) -> list[Item]:
        request = requests.get(self.baseUrl)
        htmlResult = BeautifulSoup(request.content.decode(), 'html.parser')
        request.close()

        rows = htmlResult.find_all(string=re.compile(text, flags=2))

        result: list[Item] = []
        for row in rows:
            parent = row.find_parent(name='tr')
            name = row.get_text()
            link = urljoin(self.baseUrl, row.parent.attrs['href'])
            size = parent.find(class_='size').get_text()
            
            item = Item(name, link, size)
            
            result.append(item)
        
        return result
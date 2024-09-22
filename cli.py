import db
from crawler import Crawler

class CLI():
    def __init__(self, baseUrl):
        self.crawler = Crawler(baseUrl)

    def query(self, name: str) -> None:
        items = self.crawler.query(name)
        
        for i in range(len(items)):
            print(f"{i} - {items[i].print()}")
            
        option = input("Select one or more items to save(enter 'q' to go back): ")
        
        options = option.split(sep=' ')
        
        if (len(options) <= 1 and option.lower() == 'q'):
            return
        
        if len(options) == 1:
            db.save(items[int(option)])
            return
            
        selectedItems = []
        for opt in options:
            selectedItems.append((items[int(opt)].name, items[int(opt)].link, items[int(opt)].size))
        db.save(selectedItems)
    
    def listAll(self):
        items = db.selectAll()
        
        for item in items:
            id, name, link, size, downloaded = item
            print(f'''ID: {id}\nName: {name}\nLink: {link}\nSize: {size}\nDownloaded: {downloaded == 1}\n''')
            
    def close(self):
        db.close()
        
import sqlite3

from crawler import Item

dbConn = sqlite3.connect(database='items.db')
cursor = dbConn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    link TEXT NOT NULL,
    size TEXT NOT NULL,
    downloaded INTEGER
)''')

def save(data: Item | tuple[Item]):
    if (data is None) or (isinstance(data, tuple) and len(data) == 0):
        return
    
    if isinstance(data, Item):
        cursor.execute("INSERT INTO items(name, link, size, downloaded) VALUES (?, ?, ?, FALSE)", [data.name, data.link, data.size])
    else:
        cursor.executemany("INSERT INTO items(name, link, size, downloaded) VALUES (:name, :link, :size, FALSE)", data)
    dbConn.commit()
        
def selectAll() -> list: 
    cursor.execute('SELECT * FROM items')
    return cursor.fetchall()

def selectOne(name: str):
    cursor.execute(f'SELECT * FROM items WHERE name LIKE %?%', name)
    return cursor.fetchone()
        
def close():
    cursor.close()
    dbConn.close()
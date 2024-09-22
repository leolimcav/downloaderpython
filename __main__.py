import cli
from urllib.parse import urlparse
# criar cli para consultar o site e coletar os jogos escolhidos
## 1 - buscar no site
### 1.1 - adicionar a lista
## 2 - baixar lista (acessa lista salva em sqlite)
## 3 - encerrar
baseurl = input('Enter a url: ')

cli = cli.CLI(baseurl)

while True:
    print(f'''1 - Search\n2 - List Saved\n3 - Download\n4 - Exit''')
    inputValue = input("Select: ")

    match inputValue:
        case '1':
            text = input("Type text to search: ")
            cli.query(text)
        case '2':
            cli.listAll()
        case '3':
            pass
        case '4':
            cli.close()
            break
        case _:
            print('Command not found!')
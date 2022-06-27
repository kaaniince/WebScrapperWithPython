from webscrapper_python import WebScrapper
import shelve
ws = WebScrapper()
db_name="kitaplar.db"
ws.get_soup("http://books.toscrape.com/index.html")
ws.get_categories()
ws.get_prices_stars(ws.get_soup("http://books.toscrape.com/index.html"),"http://books.toscrape.com/index.html")
ws.parse(db_name,ws.get_soup("http://books.toscrape.com/index.html"),"http://books.toscrape.com/index.html")
with shelve.open(db_name,'r') as db:
        for keys,values in db.items():
            print(keys,':',values)
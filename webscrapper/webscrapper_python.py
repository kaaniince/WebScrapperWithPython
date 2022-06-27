from bs4 import BeautifulSoup
import requests
import urllib.request as urllib2
from urllib.parse import urljoin
import shelve
class WebScrapper:
    def __init__(self):
        self.category={}
        self.category_list=[]
        self.product_info=[]
        self.category_product={}
        self.link_travel=None
    def get_soup(self,webpage):
        html=urllib2.urlopen(webpage)
        contents= html.read()
        self.soup=BeautifulSoup(contents,"html.parser")
        self.soup.prettify()
    def get_categories(self):
        list  = self.soup.find_all("ul",{"class":"nav nav-list"})
        for li in list:
            name = list[0].findChildren("a",recursive=True)
            for i in name:
                if i.string.strip()=="Books":   
                    pass
                else:
                    self.category[i.string.strip()]=i.get('href')
                    self.category_list.append(i.string.strip())
    def get_prices_stars(self,soup,link):
        soup
        list  = self.soup.find_all("ul",{"class":"nav nav-list"})
        name = list[0].findChildren("a",recursive=True)[1::]
        sayac=0
        for i in name:
            self.link_travel=i.get('href')
            link_birlesme = urljoin(link,self.link_travel)
            self.get_soup(link_birlesme)
            list2=self.soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
            for i in list2:
                name=i.h3.a.text.strip()
                price=i.find("div",{"class":"product_price"}).find_all("p")[0].text.strip().strip('£')
                url=i.h3.a.get('href')
                
                try:
                    self.product_info.append({'Name':name,'Price':price,'URL':url})
                except IndexError:
                    pass
            sayac+=1

        print(self.product_info)
        
    def create_db(self,db_ismi):
        self.prices=shelve.open(db_ismi,writeback=True,flag='c')
    def close_db(self):
        self.prices.close()
    def parse(self,db_name,soup,link):
        self.create_db(db_name)
        soup
        list  = self.soup.find_all("ul",{"class":"nav nav-list"})
        name = list[0].findChildren("a",recursive=True)[1::]
        sayac=0
        for i in name:
            self.link_travel=i.get('href')
            link_birlesme = urljoin(link,self.link_travel)
            self.get_soup(link_birlesme)
            list2=self.soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
            for i in list2:
                name=i.h3.a.text.strip()
                price=i.find("div",{"class":"product_price"}).find_all("p")[0].text.strip().strip('£')
                try:
                    self.category_product.setdefault(self.category_list[sayac], [])
                    self.category_product[self.category_list[sayac]].append({'Name':name,'Price':price})
                except IndexError:
                    pass
            sayac+=1
        print(self.category_product)
        for i,k in self.category_product.items():
            self.prices[i]=k
        self.close_db()

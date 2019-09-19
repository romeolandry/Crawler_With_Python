
import time
import requests as req
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from .CrawlerArticle import crawlerArticle
class ArticleFetcher():
    def fetch(self):
        navigation = True
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        while navigation:
            time.sleep(2)
            print (url)            
            r = req.get(url)
            doc_seite = bs(r.text,'html.parser')
            
            for card in doc_seite.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url,card.select_one("img").attrs["src"])
                
                yield crawlerArticle(title,emoji,content,image)
                
                
            nav = doc_seite.select_one(".navigation")
            if nav == None:
                navigation = False
            else:
                href = nav.select_one("a").attrs["href"]
                #page = href.split("?")[1]
                url = urljoin(url,href)
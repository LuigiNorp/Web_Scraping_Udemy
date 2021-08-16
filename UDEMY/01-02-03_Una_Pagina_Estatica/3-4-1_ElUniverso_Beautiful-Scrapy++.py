from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
#from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class News(Item):
    headliner = Field()
    description = Field()

class ElUniversoSpider(Spider):
    name = "MyFourthSpider"
    custom_settings = {
        'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    start_urls = ["https://www.eluniverso.com/deportes/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, features="lxml")
        news_container = soup.find_all('div', 'card-content | space-y-1')

        # Si hubiera otro div intermedio, aquí lo anoto
        # for container in news_container:

        #     news = container.find_all('div', 'card-content | space-y-1')
        #     # Busqué lo mismo porque todo está dentro del mismo padre
            
        for new in news_container:
            item = ItemLoader(News(), response.body)

            headliner = new.find('a').text
            
            description = new.find('p')
            # En caso de que quieras verificar si un elemento existe
            if description != None:
                description = description.text
            else:
                description = "N/A"
            #-------------------------------------------------------

            item.add_value('headliner', headliner)
            item.add_value('description', description)

            yield item.load_item()
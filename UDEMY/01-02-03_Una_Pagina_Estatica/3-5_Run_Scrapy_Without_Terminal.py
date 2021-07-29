from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

from scrapy.crawler import CrawlerProcess


class News(Item):
    headliner = Field()
    description = Field()

class ElUniversoSpider(Spider):
    name = "MyThirdSpider"
    custom_settings = {
        'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    start_urls = ["https://www.eluniverso.com/deportes/"]

    def parse(self, response):
        sel = Selector(response)
        news = sel.xpath('//div[@class="card-content | space-y-1"]')
        for new in news:
            item = ItemLoader(News(), new)
            item.add_xpath('headliner','./h2/a/text()')
            item.add_xpath('description','./p/text()')
            
            yield item.load_item()


# To run without terminal
    # This is equivalent to write in terminal: 
        # scrapy runspider file_name -o results.ext -t ext 
process = CrawlerProcess(settings={
    "FEEDS": {
        "prueba.json": {"format": "json"},
    },
})

process.crawl(ElUniversoSpider)
process.start() # the script will block here until the crawling is finished
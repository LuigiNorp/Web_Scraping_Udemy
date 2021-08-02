from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
# from scrapy.crawler import CrawlerProcess

class Hotel(Item):
    name = Field()
    price = Field()
    description = Field()
    amenities = Field()


class TripAdvisor(CrawlSpider):
    name = "Hotels"
    custom_settings = {
        'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

start_urls = ['https://www.tripadvisor.com/Hotels-g150800-Mexico_City_Central_Mexico_and_Gulf_Coast-Hotels.html']

download_delay = 2 #Seconds

rules = {

    # When the link of the website fits with the condition: (in this case) 
    # "/Hotel-Review-", it'll call to run parse function and extract data.

    Rule(
        LinkExtractor(
            allow=r'/Hotel_Review-' #To use RegEx
        ),  follow=True, callback='parse_hotel'
    )
}


def parse_hotel(self, response):
    sel = Selector(response)
    item = ItemLoader(Hotel(), sel)

    item.add_xpath('name','//h1[@id = "HEADING"]/text()')
    item.add_xpath('price','//div[contains(@class, "ui_column _")][2]/div/text()')
    item.add_xpath('description','//div[contains(@data-ssrev-handlers, "Description")]/div/div[1]/text()')
    item.add_xpath('amenities','//div[@data-test-target="amenity_text"]/text()')

    yield item.load_item()



# To run without terminal
    # This is equivalent to write in terminal: 
        # scrapy runspider file_name -o results.ext -t ext 
# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "prueba.json": {"format": "json"},
#     },
# })

# process.crawl(Hotel)
# process.start() # the script will block here until the crawling is finished
# It seems that Crawlspider manage to extract complete data of multiple elements 
# pointed by an X-Path Expression

from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

class Hotel(Item):
    name = Field()
    price = Field()
    seller = Field() 
    price_large = Field()
    seller_large = Field()
    description = Field()
    amenities = Field()


class TripAdvisor(CrawlSpider):
    name = "Hotels"
    custom_settings = {
        'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    start_urls = ['https://www.tripadvisor.com/Hotels-g150800-Mexico_City_Central_Mexico_and_Gulf_Coast-Hotels.html']

    download_delay = 2 #Seconds

    # When the link of the website fits with the condition: (in this case) 
    # "/Hotel-Review-", it'll call to run parse function and extract data.
    # Needed to use RegEx in: allow=r'pattern'
    
    rules = [Rule(LinkExtractor(allow=r'/Hotel_Review-'),  
    follow=True, callback="parse_item")]

    # Note:
    # [] Square braquets were mandatory for 
    # TypeError: 'Rule' object is not iterable

    def parse_item(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)

        prices_div = '//div[@data-vendorname]//div[contains(text(),"$") and contains(@data-sizegroup,"prices")]/text()'
        prices_a = '//a[@data-vendorname]//div[contains(text(),"$")]/text()'
        prices_a2 = '//a[@data-vendorname]//div[contains(text(),"$")][2]/text()'
        prices_span = '//span[contains(text(),"$") and contains(@title,"$")]/text()'
        sellers_div = '//div[@data-vendorname]//img[@alt]/@alt'
        sellers_a = '//a[@data-vendorname]//img[@alt]/@alt'
        sellers_span = '//div[@data-vendorname]/span[@title and not(contains(@title,"$"))]/@title'   # /div/img/@alt /a /span
        item.add_xpath('name','//h1[@id="HEADING"]/text()')
        item.add_xpath('description','//div[contains(@data-ssrev-handlers, "Description")]/div/div[1]/text()')
        item.add_xpath('amenities','//div[@data-test-target="amenity_text"]/text()')
        
        # Main Sellers and Prices
        if sellers_a != None:
            item.add_value('seller', response.xpath(sellers_a).extract())
        if sellers_div != None:
            item.add_value('seller', response.xpath(sellers_div).extract())

        if prices_a2 != None:
            item.add_xpath('price', prices_a2)
        if prices_a != None:
            item.add_xpath('price', prices_a)
        if prices_div != None:
            item.add_xpath('price', prices_div)


        # Other Options
        item.add_xpath('price_large', prices_span)
        item.add_xpath('seller_large', sellers_span)
    
        yield item.load_item()

# To run without terminal
    # This is equivalent to write in terminal: 
        # scrapy runspider file_name -o results.ext -t ext 
process = CrawlerProcess(settings={
    "FEEDS": {
        "4-3-1_MercadoLibre_Paging.json": {"format": "json"},
    },
})

process.crawl(TripAdvisor)
process.start() # the script will block here until the crawling is finished





# ------------------------------ HISTORIAL --------------------------------
# Versión:      2
# Descripción:  Intentaré hacer un parseo dentro de otro parseo, a ver si la infomación
              # obtenida resulta como espero []: SPOILER: No funcionó (Scrapy no puede
              # agregar tuplas dentro de los archivos)

# from scrapy.item import Field, Item
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.selector import Selector
# from scrapy.loader.processors import MapCompose
# from scrapy.linkextractors import LinkExtractor
# from scrapy.loader import ItemLoader
# from scrapy.crawler import CrawlerProcess

# class Hotel(Item):
#     name = Field()
#     seller = Field()
#     price = Field()
#     description = Field()
#     amenities = Field()


# class TripAdvisor(CrawlSpider):
#     name = "Hotels"
#     custom_settings = {
#         'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
#     }
#     start_urls = ['https://www.tripadvisor.com/Hotels-g150800-Mexico_City_Central_Mexico_and_Gulf_Coast-Hotels.html']

#     download_delay = 2 #Seconds

#     # When the link of the website fits with the condition: (in this case) 
#     # "/Hotel-Review-", it'll call to run parse function and extract data.
#     # Needed to use RegEx in: allow=r'pattern'
    
#     rules = [Rule(LinkExtractor(allow=r'/Hotel_Review-'),  
#     follow=True, callback="parse_item")]

#     # Note:
#     # [] Square braquets were mandatory for 
#     # TypeError: 'Rule' object is not iterable

#     def parse_item(self, response):
#         sel = Selector(response)
#         item = ItemLoader(Hotel(), sel)
      
#         if '//div[contains(@class, "ui_column _")][2]/div/text()' != None:
#             item.add_xpath('name','//h1[@id="HEADING"]/text()')
#             item.add_xpath('description','//div[contains(@data-ssrev-handlers, "Description")]/div/div[1]/text()')
#             item.add_xpath('amenities','//div[@data-test-target="amenity_text"]/text()')

#             # sellers = sel.xpath('//div[@data-vendorname]//div[contains(text(),"$")]')
#             # sellers = sel.xpath('//div[@data-vendorname]/child::span[contains(@title,"$")]')
#             # sellers = '//div[@data-vendorname]'
            
#             sellers = '//div[@data-vendorname]//div[contains(text(),"$") and contains(@data-sizegroup,"prices")]|//span[contains(text(),"$") and contains(@title,"$")]'
#             prices1 = '//div[@data-vendorname]//img[@alt]|//a[@data-vendorname]//img[@alt]'   # /div /a
#             prices2 = '//div[@data-vendorname]//span[@title and not(contains(@title,"$"))]'

#             print((response.xpath(prices1)).count())

#             # //div[@data-vendorname]//img[@alt]|//div[@data-vendorname]//span[@title and not(contains(@title,"$"))]
            
#             # for price1 in prices1:
#             #     item.add_value('price', response.xpath(prices1+'/@alt').extract())
            
#             # for price2 in prices2:
#             #     item.add_xpath('price', prices2+'/text()')

#             # for seller in sellers:
#             #     item.add_value('seller', response.xpath(sellers+'/@data-vendorname').extract())
                 
#         yield item.load_item()

# # To run without terminal
#     # This is equivalent to write in terminal: 
#         # scrapy runspider file_name -o results.ext -t ext 
# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "4-3-1_MercadoLibre_Paging.json": {"format": "json"},
#     },
# })

# process.crawl(TripAdvisor)
# process.start() # the script will block here until the crawling is finished


# -------------------------------------------------------------------------

# Versión:      1
# Descripción:  Esta versión extrae correctamente de casi la totalidad de 
#               los datos, a excepción de la información del vendedor.

# from scrapy.item import Field, Item
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.selector import Selector
# from scrapy.loader.processors import MapCompose
# from scrapy.linkextractors import LinkExtractor
# from scrapy.loader import ItemLoader
# from scrapy.crawler import CrawlerProcess

# class Hotel(Item):
#     name = Field()
#     seller = Field()
#     price = Field()
#     description = Field()
#     amenities = Field()

# class TripAdvisor(CrawlSpider):
#     name = "Hotels"
#     custom_settings = {
#         'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
#     }
#     start_urls = ['https://www.tripadvisor.com/Hotels-g150800-Mexico_City_Central_Mexico_and_Gulf_Coast-Hotels.html']

#     download_delay = 2 #Seconds

#     # When the link of the website fits with the condition: (in this case) 
#     # "/Hotel-Review-", it'll call to run parse function and extract data.
#     # Needed to use RegEx in: allow=r'pattern'
    
#     rules = [Rule(LinkExtractor(allow=r'/Hotel_Review-'),  
#     follow=True, callback="parse_item")]

#     # Note:
#     # [] Square braquets were mandatory for 
#     # TypeError: 'Rule' object is not iterable

#     def parse_item(self, response):
#         sel = Selector(response)
#         item = ItemLoader(Hotel(), sel)

#         if '//div[contains(@class, "ui_column _")][2]/div/text()' != None:
#             item.add_xpath('name','//h1[@id="HEADING"]/text()')
#             item.add_xpath('description','//div[contains(@data-ssrev-handlers, "Description")]/div/div[1]/text()')
#             item.add_xpath('amenities','//div[@data-test-target="amenity_text"]/text()')

#             sellers = sel.xpath('//div[@data-vendorname]/span[2]/text()')
    
#             for sell in sellers:
#                 item.add_xpath('seller','//div[@data-vendorname]/child::span[not(contains(@title,"$"))]/text()')
#                 item.add_xpath('price','//div[@data-vendorname]/span[contains(@title,"$")]/text()')

#         yield item.load_item()


# # To run without terminal
#     # This is equivalent to write in terminal: 
#         # scrapy runspider file_name -o results.ext -t ext 
# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "4-3-1_MercadoLibre_Paging.json": {"format": "json"},
#     },
# })

# process.crawl(TripAdvisor)
# process.start() # the script will block here until the crawling is finished


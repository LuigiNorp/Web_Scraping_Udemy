from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class News(Item):
    title = Field()
    description = Field()

class ElUniversalSpider(Spider):
    name = "MySecondSpider"
    custom_settings = {
        'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }

    start_urls = ["https://www.eluniversal.com.mx/nacion"]

    def parse(self, response):
        sel = Selector(response)
        news = sel.xpath('(//ancestor::div[h2]|//ancestor::div[article]|//div[@class="per-Tipo3"]//ancestor::div[h3])')

        for new in news:
            item = ItemLoader(News(), new)

            title = './h2/a'
            description = './/h3/a'

            item.add_xpath('title', title + "/text()")
            
            if description != None:
                item.add_xpath('description', description + "/text()")
            else:
                item.add_xpath('description', './p/text()')

            yield item.load_item()



# 'choose(contains(@h3,"")),"./h3/text()",


# Como checar si un tag en X-Path existe:

            #isExist = sel.xpath(boolean('./h3')

            #print(isExists)

    #response.xpath('//div[@id="not-exists"]/text()').extract_first() is None
    #isExists = response.xpath("./h3").extract_first(default='not-found')

# Otros intentos de X-Path
        #item.add_xpath("title",".//h2[@class='ce3-Tipo1_Titulo uniplus']/a/text()")

        #item.add_xpath("question", ".//h3/a/text()")
        #item.add_xpath("description", ".//div[@class='excerpt']/text()")
        #item.add_value("id", 1)

        #news = sel.xpath('//div[@class="contenido-principal"]//div[not contains(@class, "gl-Grid_3")]//h2')
        #news = sel.xpath('//div[@class="gl-Grid_9"]//div[@class=contains(@class,"otas")]')
        #news = sel.xpath('//div[@class="gl-Grid_9"]//div[@class=contains(@h2,"itulo")]//')


#  ----------------------------- HISTORIAL ----------------------------------

# 22/07/2021:

# from scrapy.item import Field
# from scrapy.item import Item
# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scrapy.loader import ItemLoader

# class News(Item):
#     title = Field()
#     description = Field()

# class ElUniversalSpider(Spider):
#     name = "MySecondSpider"
#     custom_settings = {
#         'USER_AGENT':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
#     }

#     start_urls = ["https://www.eluniversal.com.mx/nacion"]

#     def parse(self, response):
#         sel = Selector(response)
#         news = sel.xpath('(//ancestor::div[h2]|//ancestor::div[article]|//div[@class="per-Tipo3"]//ancestor::div[h3])')

#         for new in news:
#             item = ItemLoader(News(), new)
#             item.add_xpath('title', './h2/a/text()')
#             item.add_xpath('description', './p/text()')

#             yield item.load_item()
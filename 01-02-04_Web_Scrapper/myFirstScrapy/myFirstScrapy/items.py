# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstscrapyItem(scrapy.Item):

    # define the fields for your item here like:
    location = scrapy.Field()
  
  
    def parse_item(self, response):
        item_links = response.css('.text > .listing-company > .list-location > a::text').extract()
        
        for x in item_links:
            yield scrapy.Request(x, callback=self.MyfirstscrapyItem)




                            # Using CSS

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class JobsSpider(CrawlSpider):
    name = 'jobs'
    allowed_domains = ['www.python.org']
    start_urls = ['http://www.python.org/',
                  'https://www.python.org/jobs/']

    rules = (Rule(LinkExtractor(allow=(), 
                            restrict_css=('.list-recent-jobs',)),
                            callback="parse_item",
                            follow=True),)

    def parse_item(self, response):
        print('Extracting…' + response.url)



                            # Using X-PATH

from scrapy.selector import Selector
from scrapy.item import Item

body = '<html><body><h1>Heading 1</h1></body></html>'
Selector(text = body).xpath('//h1/text()').get()

class Job(Item):
    from scrapy.item import Field
    company = Field()
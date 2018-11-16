import scrapy

from scrapy.http import Response

class TestSpider(scrapy.Spider):
    name = "prac_spider"
    allowed_domains = ['superdatascience.com']
    start_urls = ['https://www.superdatascience.com/scrapy_practical/']
    
    
    def parse(self, response):
        item = {
                'logo': response.css('#header > div > div >a >img').xpath('@src').extract(),
                'Q1':   response.css('#content > div.entry-content > h3.sc1::text').extract(),
                }
        self.logger.info('aaa %s', item)
        return item






#()[0][:-1]

 #//*[@id="header"]/div/div/a/img
 # //*[@id="content"]/div[1]/h3[1]

 # run scrapy runspider pracspider.py -o data.csv


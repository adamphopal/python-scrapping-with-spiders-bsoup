# -*- coding: utf-8 -*-
import scrapy


class BruinSpider(scrapy.Spider):
    name = 'bruin'
    #allowed_domains = ['hamims-books.herokuapp.com']
    start_urls = ['http://hamims-books.herokuapp.com']
    
    def parse(self, response):
        urls = response.css('div.col-md-4 > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
            
    def parse_details(self, response):
    	tables = response.css('table.bruin-table').extract()
    	for table in tables:
            yield {
                'author': response.css('td::text').extract(),
            }
            
           
        
        
        	
        
        
            
        

    

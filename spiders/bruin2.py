# -*- coding: utf-8 -*-
import scrapy


class BruinSpider(scrapy.Spider):
    name = 'bruin'
    allowed_domains = ['hamims-books.herokuapp.com']
    start_urls = ['http://hamims-books.herokuapp.com/']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for bruin in response.css('div.col-md-4'):
            item = {
                'bruin_title': bruin.css('h3.panel-title::text').extract(),
                'bruin_username': bruin.css('a.panel-username::text').extract(),
                'username_link': bruin.css('a.panel-username::attr(href)').extract(),
            }
            yield item

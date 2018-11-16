# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class NewItem(scrapy.Item):
	main_headline = Field()
	headline = Field()
	
	url = Field()
	project = Field()
	spider = Field()
	server = Field()
	date = Field()


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
    
    
class BlogItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()


class MovieItem(scrapy.Item):
	title = scrapy.Field()
	directors = scrapy.Field()
	
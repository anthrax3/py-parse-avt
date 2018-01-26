# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AvitosItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    #price_clear = scrapy.Field()
    link = scrapy.Field()
    #describe = scrapy.Field()
    #name_seller = scrapy.Field()
    #tel_seller = scrapy.Field()
    

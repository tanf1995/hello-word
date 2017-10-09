# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    post_name = scrapy.Field()
    company_name = scrapy.Field()
    pay = scrapy.Field()
    location = scrapy.Field()

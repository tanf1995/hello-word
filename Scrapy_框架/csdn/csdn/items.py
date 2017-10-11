# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    question = scrapy.Field()
    content = scrapy.Field()
    answer_num = scrapy.Field()
    question_url = scrapy.Field()

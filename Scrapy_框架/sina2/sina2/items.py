# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Sina2Item(scrapy.Item):
    # 大类标题
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()

    # 小类标题
    child_title = scrapy.Field()
    child_url = scrapy.Field()

    # 小目录路径，存放文章时使用
    child_loc = scrapy.Field()

    # 每篇文章的字段
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pub_time = scrapy.Field()

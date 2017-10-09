# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

class DouyuImageSpider(scrapy.Spider):
    name = 'douyu_image'
    allowed_domains = ['capi.douyucdn.cn']
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 返回从json里获取 data段数据集合
        data = json.loads(response.text)["data"]

        for each in data:
            item = DouyuItem()
            item["name"] = each["nickname"]
            item["imagesUrls"] = each["vertical_src"]

            yield item

        self.offset += 100
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

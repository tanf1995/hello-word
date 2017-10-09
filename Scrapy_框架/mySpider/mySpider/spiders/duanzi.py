# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DuanziItem
import time


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['http://neihanshequ.com/']
    # http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1507451345.81
    start_urls = ['http://neihanshequ.com/']

    # for i in range(3):
    #     t = time.time()
    #     data = int(t*100)/100
    #     start_urls.append('http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=' + str(data))
    #     time.sleep(0.5)

    def parse(self, response):
        duanzi_list = response.xpath('//div[@class="detail-wrapper"]')

        # all_duanzi = []
        for duanzi in duanzi_list:
            item = DuanziItem()

            author_name = duanzi.xpath('.//span[@class="name"]/text()').extract()
            content = duanzi.xpath('.//p/text()').extract()

            item['author_name'] = author_name[0]
            item['content'] = content[0]

            yield item
            # all_duanzi.append(item)

        # return all_duanzi




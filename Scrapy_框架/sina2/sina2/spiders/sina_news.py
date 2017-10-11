# -*- coding: utf-8 -*-
import scrapy
import os
from sina2.items import Sina2Item

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        parent_titles = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]/a/text()').extract()
        parent_urls = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]/a/@href').extract()

        child_titles = response.xpath('//div[@id="tab01"]//ul[@class="list01"]/li/a/text()').extract()
        child_urls = response.xpath('//div[@id="tab01"]//ul[@class="list01"]/li/a/@href').extract()

        items = []
        for par_index in range(len(parent_urls)):
            # 创建大类目录
            par_direct = os.path.join('Datas', parent_titles[par_index])
            # par_direct = "./Datas/" + parent_titles[par_index].encode('utf-8')
            if not os.path.exists(par_direct):
                os.makedirs(par_direct)

            for chi_index in range(len(child_urls)):
                # 判断此小类是否属于当前大类
                is_belong = child_urls[chi_index].startswith(parent_urls[par_index])
                if is_belong:
                    item = Sina2Item()
                    item['parent_title'] = parent_titles[par_index]
                    item['parent_url'] = parent_urls[par_index]

                    item['child_title'] = child_titles[chi_index]
                    item['child_url'] = child_urls[chi_index]

                    # 创建小目录
                    chi_direct = os.path.join(par_direct, child_titles[chi_index])
                    # chi_direct = par_direct + '/'+ child_titles[chi_index].encode('utf-8')
                    item['child_loc'] = chi_direct
                    if not os.path.exists(chi_direct):
                        os.makedirs(chi_direct)

                    items.append(item)

        for item in items:
            yield scrapy.Request(url=item['child_url'], meta={'meta_1': item}, callback=self.sencode_parse)

    # 进入小类标题页面
    def sencode_parse(self, response):
        meta_1 = response.meta['meta_1']

        articles_urls = response.xpath('//a/@href').extract()

        items = []
        for url in articles_urls:
            # 判断连接是否为新闻文章
            is_belong = url.endswith('.shtml') and url.startswith(meta_1['parent_url'])
            if is_belong:
                item = Sina2Item()
                item['url'] = url

                item['parent_title'] = meta_1['parent_title']
                item['parent_url'] = meta_1['parent_url']
                item['child_title'] = meta_1['child_title']
                item['child_url'] = meta_1['child_url']
                item['child_loc'] = meta_1['child_loc']

                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['url'], meta={'meta_2': item}, callback=self.dealart_parse)

    def dealart_parse(self, response):
        meta_2 = response.meta['meta_2']

        item = Sina2Item()
        item['parent_title'] = meta_2['parent_title']
        item['parent_url'] = meta_2['parent_url']
        item['child_title'] = meta_2['child_title']
        item['child_url'] = meta_2['child_url']
        item['child_loc'] = meta_2['child_loc']

        title = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()
        if len(title) != 0:
            item['title'] = title[0]
        else:
            item['title'] = 'unknow'

        contents = response.xpath('//div[@id="artibody"]/p/text()').extract()
        if len(contents) != 0:
            item['content'] = "".join(contents)
        else:
            item['content'] = 'unknow'

        pub_time = response.xpath('//span[@class="time-source"]/text()').extract()
        if len(pub_time) != 0:
            item['pub_time'] = pub_time[0]
        else:
            item['pub_time'] = 'unknow'

        yield item
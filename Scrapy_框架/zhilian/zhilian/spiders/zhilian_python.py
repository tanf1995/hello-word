# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhilian.items import ZhilianItem


class ZhilianPythonSpider(CrawlSpider):
    name = 'zhilian_python'
    allowed_domains = ['sou.zhaopin.com']
    # http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=python&p=1 成都地区python
    # http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=python&p=1 全国python
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%88%90%E9%83%BD&kw=python&p=1']

    rules = (
        Rule(LinkExtractor(allow=(r'http://sou.zhaopin.com')), callback='parse_zhilian', follow=True),
    )

    def parse_zhilian(self, response):
        info = response.xpath('//table[@class="newlist"]')
        print info
        for each in info[1:]:
            item = ZhilianItem()
            item["post_name"] = each.xpath('.//td[@class="zwmc"]//a[@style="font-weight: bold"]/text()').extract()[0]
            item["company_name"] = each.xpath('.//td[@class="gsmc"]/a/text()').extract()[0]
            item["pay"] = each.xpath('.//td[@class="zwyx"]/text()').extract()[0]
            item["location"] = each.xpath('.//td[@class="gzdd"]/text()').extract()[0]

            yield item


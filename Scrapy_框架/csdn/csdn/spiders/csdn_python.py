# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from csdn.items import CsdnItem


class CsdnPythonSpider(CrawlSpider):
    name = 'csdn_python'
    allowed_domains = ['bbs.csdn.net']
    start_urls = ['http://bbs.csdn.net/forums/OL_Script?page=1']

    page_links = LinkExtractor(allow=r'/forums/OL_Script\?page=')

    rules = (
        Rule(page_links),
        Rule(LinkExtractor(allow=r'/topics/\d+'), callback='parse_item', follow=False)
    )

    # 处理回去的连接，如若需要 process_links='deal_links'
    # def deal_links(self, links):
    #     for each in links:
    #         each.url = 'http://bbs.csdn.net' + each.url
    #     return links

    def parse_item(self, response):
        item = CsdnItem()
        item['question'] = response.xpath('//div[@class="detail_title"]/h1/span/text()').extract()[0]
        content = response.xpath('//div[@class="detailed"]/table')[0].xpath('.//div[@class="post_body"]/text()').extract()
        item['content'] = "".join(content).strip().replace("\n", "").replace(" ", "")
        item['answer_num'] = response.xpath('//span[@class="return_time"]/text()').extract()[0]
        item['question_url'] = response.url

        yield item


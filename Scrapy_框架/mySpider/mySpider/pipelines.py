# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DuanziPipeline(object):
    def __init__(self):
        self.file = open('duanzi.json', 'w')
        self.count = 1

    # 必要的方法，处理
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False).encode('utf-8')
        self.file.write(str(self.count) + '\n' + content + '\n')
        self.count += 1

    # 类的关闭方法，可选
    def close_spider(self, spider):
        self.file.close()

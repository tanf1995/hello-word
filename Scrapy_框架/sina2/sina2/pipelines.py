# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

class Sina2Pipeline(object):
    def process_item(self, item, spider):
        filename = os.path.join(item['child_loc'], item['title']) + '.txt'
        with open(filename, 'w') as f:
            f.write(item['content'].encode('utf-8'))
            f.write('\n' + item['pub_time'].encode('utf-8'))

        return item

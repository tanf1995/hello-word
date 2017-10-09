#coding=utf-8

import urllib2
from lxml import etree
import json

url = "https://www.qiushibaike.com/hot/"
headers = {
    # chrome浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}

request = urllib2.Request(url=url, headers=headers)
html = urllib2.urlopen(request).read()

selector = etree.HTML(html)
# 段子节点
node_list = selector.xpath('//div[contains(@id, "qiushi_tag_")]')
for node in node_list:
    # 作者
    name = node.xpath('.//h2')[0].text
    # 内容
    content = node.xpath('.//div[@class="content"]/span')[0].text
    # 点赞数
    vote = node.xpath('.//span[@class="stats-vote"]/i')[0].text
    # 评论数
    comment = node.xpath('.//span[@class="stats-comments"]//i')[0].text
    # 图片
    img = node.xpath('./div[@class="thumb"]//img/@src')

    item = {
        "name": name,
        "content": content,
        "vote": vote,
        "comment": comment,
        "img": img
    }
    filename = "糗事百科json"
    with open(filename.decode('utf-8'), "a") as f:
        f.write(json.dumps(item, ensure_ascii=False).encode('utf-8') + '\n')
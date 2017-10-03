import urllib.request
import urllib.parse
import os
import re
from lxml import etree

class Spider(object):
    def __init__(self):
        # 百度贴吧
        self.dirname = ''
        self.load_count = 0
        self.url = 'https://tieba.baidu.com/f?'
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"}


    def loadPage(self):
        # 下载网页
        tieba_name = input('贴吧名：')
        self.dirname = tieba_name
        # 创建用来保存图片的文件夹
        os.mkdir(self.dirname)
        start_page = int(input('起始页：'))
        end_page = int(input('结束页：'))
        for page in range(start_page, end_page+1):
            tieba_url = self.url + urllib.parse.urlencode({'kw': tieba_name, 'pn': str((page-1)*50)})
            request = urllib.request.Request(url=tieba_url, headers=self.header)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf-8')
            # 将网页解译为xml格式
            # selector = etree.HTML(html)
            # article_link = selector.xpath('//a/@id')
            # '//div[@class="t_con cleafix"]/div/div/div/a[@class="j_th_tit "]/@href'

            #用正则表达式
            rex = '<div\sclass="t_con\scleafix">.*?<div\s.*?>.*?<a\shref="(.*?)"\stitle=".*?"\starget="_blank"\sclass="j_th_tit\s".*?</a>.*?</div>'
            pattern1 = re.compile(rex, re.S)
            article_link = pattern1.findall(html)
            for a_link in article_link:
                full_link = 'https://tieba.baidu.com' + a_link
                self.entry_article(full_link)


    def entry_article(self, a_link):
        response = urllib.request.urlopen(a_link)
        html = response.read().decode('utf-8')
        selector = etree.HTML(html)
        # 静态图的匹配规则
        img_link = selector.xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')
        # 动态图的匹配规则
        #img_link = selector.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src')
        for i_link in img_link:
            img_name = a_link[-5:] + i_link[-10:]
            self.load_img(i_link, img_name)


    def load_img(self, i_link, img_name):
        # 保存图片
        response = urllib.request.urlopen(i_link)
        img = response.read()
        file = os.path.join(self.dirname, img_name)
        with open(file, 'wb') as i:
            i.write(img)
        self.load_count += 1
        print('----图片%s下载完成---'%img_name)



    def control(self):
        # 控制是否继续
        self.loadPage()
        print('总共下载%d张图片'%self.load_count)

if __name__ == '__main__':
    s = Spider()
    s.control()
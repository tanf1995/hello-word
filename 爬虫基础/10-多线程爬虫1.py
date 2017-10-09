import threading
import urllib.request
from queue import Queue
from lxml import etree
import json
import time

def main():
    collect_threads_name = ['采集线程1号', '采集线程2号', '采集线程3号']
    parse_threads_name = ['解析线程1号', '解析线程2号', '解析线程3号']
    cQueue = Queue(10)
    for i in range(1, 11):
        cQueue.put(i)
    pQueue = Queue()

    # 采集线程
    collect_threads = []
    for ct in collect_threads_name:
        cols = CollectSpider(ct, cQueue, pQueue)
        cols.start()
        collect_threads.append(cols)

    while not cQueue.empty():
        pass
    global COLLECT_EXIT
    COLLECT_EXIT = True

    for thread in collect_threads:
        thread.join()
        print('-----1----')

    # 解析线程
    lock = threading.Lock()
    parse_threads = []
    file = open('糗事百科.txt', 'a')
    for pt in parse_threads_name:
        pars = ParseSpider(pt, pQueue, lock, file)
        pars.start()
        parse_threads.append(pars)

    while not pQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in parse_threads:
        thread.join()
        print('-----2-----')

    with lock:
        file.close()
    # lock.acquire()
    # file.close()
    # lock.release()

    print('thank you to use!')

class CollectSpider(threading.Thread):
    def __init__(self, name, cQueue, pQueue):
        super(CollectSpider, self).__init__()
        self.name = name
        self.cQueue = cQueue
        self.pQueue = pQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        self.url = 'https://www.qiushibaike.com/hot/page/'

    def run(self):
        print('%s开始工作' % self.name)
        while not COLLECT_EXIT:
            try:
                page = self.cQueue.get(block=False)
                url = self.url + str(page) + '/'
                request = urllib.request.Request(url=url, headers=self.headers)
                html = urllib.request.urlopen(request).read().decode('utf-8')
                time.sleep(1)
                self.pQueue.put(html)
            except Exception:
                pass
        print('%s工作完成'%self.name)


class ParseSpider(threading.Thread):
    def __init__(self, name, pQueue, lock, file):
        super(ParseSpider, self).__init__()
        self.name = name
        self.pQueue = pQueue
        self.lock = lock
        self.file = file

    def run(self):
        print('%s开始工作' % self.name)
        while not PARSE_EXIT:
            try:
                html = self.pQueue.get(block=False)
                selector = etree.HTML(html)
                node_list = selector.xpath('//div[contains(@id, "qiushi_tag_")]')
                for node in node_list:
                    # 作者
                    name = node.xpath('.//h2')[0].text
                    # 内容
                    content_list = node.xpath('.//div[@class="content"]/span')
                    content = ''
                    for num in range(len(content_list)):
                        content += content_list[num].text
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

                    # 打开、关闭锁
                    with self.lock:
                       self.file.write(json.dumps(item, ensure_ascii=False) + '\n\n')
                    # self.lock.acquire()
                    # self.file.write(json.dumps(item, ensure_ascii=False) + '\n')
                    # self.lock.release()

            except Exception:
                pass
        print('%s工作完成' % self.name)


COLLECT_EXIT = False
PARSE_EXIT = False





if __name__ == '__main__':
    main()
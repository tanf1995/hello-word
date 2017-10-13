#coding=utf-8

import tornado.web
import tornado.ioloop
from tornado.httpserver import HTTPServer
import time

class Indexhandler(tornado.web.RequestHandler):
    def get(self):
        count = self.get_cookie('page_count')
        if not count:
            self.set_cookie('page_count', '0')
            count = 0
        else:
            count = int(count) + 1
            self.set_cookie('page_count', str(count))
        # self.set_cookie('tanfeng', '123456', path='/',\
                        # expires=time.mktime(time.strptime('2017-10-13 23:59:59', '%Y-%m-%d %H:%M:%S')))
        self.write('你已经访问本站%d次'%count)

class Delcookie(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie('page_count')
        self.write('删除cookies成功')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'^/$', Indexhandler),
        (r'^/del_cookie$', Delcookie)
    ], debug=True)

    http_server = HTTPServer(app)
    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()
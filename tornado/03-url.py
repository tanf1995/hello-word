# coding=utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.web import url, RequestHandler

class Indexhandler(RequestHandler):
    def get(self, *args, **kwargs):
        js_url = self.reverse_url('js_url') # 导入url
        self.write('首页!,' + '<a href="%s">js</a>'%js_url)


class Pythonhandler(RequestHandler):
    def initialize(self, name): # 接受rul传来的参数
        self.name = name

    def get(self):
        id = self.get_query_argument("id", default=10)  # GET请求的参数获取
        self.write(id)

    # def post(self, *args, **kwargs):
    #     idnum = self.get_argument("id")
    #     self.write(idnum)


class Jshandler(RequestHandler):
    def get(self, num):
        self.write(num)


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', Indexhandler),
        (r'/python/', Pythonhandler, {'name': 'python'}),
        url(r'/js/', Pythonhandler, {'name': 'js'}, name='js_url'), # 为url取名
        (r'/js/(?P<num>\d+)', Jshandler),  # 截取命名url中的值
    ], debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)

    tornado.ioloop.IOLoop.current().start()
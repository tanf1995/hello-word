#coding=utf-8
import sys
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.web import RequestHandler, url, StaticFileHandler
import os

# 当前文件所在路径
current_path = os.path.dirname(__file__)
tornado.options.define('port', default=8000, type=int, help='端口')

class Indexhandler(RequestHandler):
    def get(self):
        context = {
            'price1': 500,
            'price2': 300,
            'price3': 100
        }
        addr = ['宽窄巷子', '南山路', '延安西路']
        # 传入列表和字典，渲染模板
        self.render('index.html', addr=addr, **context)
        # 模板内的用法和django基本差不多


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = tornado.web.Application([
        # 处理首页
        (r'^/$', Indexhandler)
        # 绝对路径的方式访问首页
        # (r'^/()$', StaticFileHandler, {'path': os.path.join(current_path, 'static/html'.decode('utf-8')), 'default_filename': 'index.html'})
    ],
    # 指定静态文件目录
    static_path=os.path.join(current_path, "static".decode('utf-8')),
    # 指定模板目录
    template_path = os.path.join(current_path, "templates".decode('utf-8')),
    debug=True
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
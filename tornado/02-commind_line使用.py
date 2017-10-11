#coding=utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# 全局设置接受的值，动态绑定端口
tornado.options.define('port', default=8000, type=int, help='端口')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('welcome to tornado!')

if __name__ == '__main__':
    # 接受全局变量的值
    tornado.options.parse_command_line()
    print tornado.options.options.port

    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
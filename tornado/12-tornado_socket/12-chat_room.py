# coding=utf-8
import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler
from tornado.httpserver import HTTPServer
import tornado.options
from tornado.websocket import WebSocketHandler
import os
import datetime

tornado.options.define('port', 8000, type=int, help='端口')

# 首页
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class ChatHandler(WebSocketHandler):
    users = set()  # 集合用来存储用户

    def open(self, *args, **kwargs):
        if self.check_user(self.request):
            self.users.add(self)  # 建立连接后添加用户到集合
            for user in self.users:  # 广播新用户上线通知
                user.write_message(u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')))
        print self.users

    # 去掉重复登录的ip
    def check_user(self, now_user):
        for user in self.users:
            if now_user.remote_ip == user.request.remote_ip:
                return False
        return True

    def on_message(self, message):
        for user in self.users:  # 广播新消息
            user.write_message(u"[%s]-[%s]: %s" % (self.request.remote_ip, datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), message))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message(u"[%s]-[%s]-离开聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')))

    def check_origin(self, origin):
        return True  # 允许websocket跨域请求

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/chat', ChatHandler),
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            template_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True
        )
        super(Application, self).__init__(handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()

    http_server = HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    print '启动成功'

    tornado.ioloop.IOLoop.current().start()
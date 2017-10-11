#coding=utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver

class Indexhandler(tornado.web.RequestHandler):
    # 树立get请求
    def get(self, *args, **kwargs):
        self.write('welcome to tornado!')

if __name__ == '__main__':
    app = tornado.web.Application([
        # 配置路由和处理的类
        (r'/', Indexhandler),
    ])

    # 绑定端口， 只能在单进程中使用
    # app.listen(8000)

    # 手动配置服务器
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)

    # 开启多进程
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.bind(8000)
    # http_server.start(num_processes=0)  # 参数为0表示使用系统cpu核数，若大于0则开始参数个进程

    # 返回当前IOLoop实例， 并且开启当前实例的I/O循环并启动监听
    tornado.ioloop.IOLoop.current().start()
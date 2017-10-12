#coding=utf-8
import sys
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.web import RequestHandler, url, StaticFileHandler
import torndb
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

    def post(self):
        # 数据库插入数据
        title = self.get_argument('title')
        position = self.get_argument('position')
        price = self.get_argument('price')
        score = self.get_argument('score')
        comments = self.get_argument('comments')
        try:
            # 返回插入后本行id也是最后一行
            ret = self.application.db.execute(\
                "insert into houses(title, position, price, score, comments) values(%s, %s, %s, %s, %s)"\
                %(title, position, price, score, comments))
            # 返回影响的行数
            # ret = self.application.db.execute_rowcount(...)
        except Exception as e:
            self.write("Error: %s"%e)
        else:
            self.write('保存成功： %d'%ret)


class Gethandler(RequestHandler):
    def get(self):
        hid = self.get_argument('id')
        try:
            # 返回单行数据
            ret = self.application.db.get("select title,position,price,score,comments from hourses where id=%d"%hid)
            #返回多行数据
            # ret = self.application.db.query("select title,position,price,score,comments from hourses where id=%d"%hid)
        except Exception as e:
            self.write('error: %s'%e)
        else:
            self.write('index.html', hourse=[ret])


# 继承的app类
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'^/$', Indexhandler)
        ]

        settings = dict(
            static_path = os.path.join(current_path, "static".decode('utf-8')),
            template_path=os.path.join(current_path, "templates".decode('utf-8')),
            debug=True
        )

        super(Application, self).__init__(handlers, **settings)
        # 连接MySQL数据库
        self.db = torndb.Connection(
            host='localhost',
            database='tornado1',
            user='root',
            password='951021'
        )


if __name__ == '__main__':
    print 'OK'
    tornado.options.parse_command_line()

    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
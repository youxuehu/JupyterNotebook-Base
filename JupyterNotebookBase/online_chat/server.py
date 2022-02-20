# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os,json
import datetime
from JupyterNotebookBase import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.websocket import WebSocketHandler

class IndexHandler(RequestHandler):
    def get_current_user(self):
        '''
        重写RequestHandler类中的get_current_user方法，用来判断当前是否是登录状态，请求中所有被@tornado.web.authenticated 装饰的方法，都需要此方法返回值不为None，否则给与403拒绝
        :return: 用户名或者None . 为None判断为非法请求，POST 时Tornado进行403禁止访问 ；GET 时 302 重定向到/login
        '''
        user = self.get_argument(name='username',default='None')
        if user and user != 'None':
            print('IndexHandler类 get_current_user获取到用户:',user)
            return user

    @tornado.web.authenticated   #确认请求合法 依赖于get_current_user(self):函数的返回值作为判断请求是否合法
    def get(self):
        print("IndexHandler 收到GET请求")
        self.render("online_index.html",current_user=self.current_user)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        print('IndexHandler 收到POST请求')
        self.render("online_index.html", current_user=self.current_user)

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        '''
        处理输入昵称界面get请求
        :param args:
        :param kwargs:
        :return:
        '''
        cookie_value = self.get_secure_cookie('count')
        print('cookie_value :', cookie_value)
        count = int(cookie_value) + 1 if cookie_value else 1
        self.set_secure_cookie("count", str(count))  # 设置一个带签名和时间戳的cookie，防止cookie被伪造。

        #使用ajax方法做的前端
        # self.render('login_use_ajax.html')
        #使用form表单提交数据 的前端
        self.render('login_use_form.html')
    def post(self, *args, **kwargs):
        '''
        暂时用不到
        :param args:
        :param kwargs:
        :return:
        '''
        pass


class ChatHandler(WebSocketHandler):
    def get_current_user(self):
        user = self.get_argument(name='username',default='None')
        if user and user != 'None':
            return user

    users = set()  # 用来存放在线用户的容器
    @tornado.web.authenticated
    def open(self):
        print('收到新的WebSocket连接')
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:  # 向已在线用户发送消息
            u    .write_message(u"[%s]-[%s]-%s 进入聊天室" % (
    self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.current_user))

    def on_message(self, message):
        message = json.loads(message)
        print(type(message),message)
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"[%s]-[%s]-说：<br> &nbsp&nbsp&nbsp&nbsp%s" % ( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.current_user,message.get('msg')))

    def on_close(self):
        self.users.remove(self) # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message(u"[%s]-[%s]-%s 离开聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.current_user))

    def check_origin(self, origin):
        return True


if __name__ == '__main__':
    tornado.options.parse_command_line()
    settings = {
        "template_path": DEFAULT_TEMPLATE_PATH_LIST,
        "static_path": DEFAULT_STATIC_FILES_PATH,
        "websocket_ping_interval": 5,
        "login_url": "/login",
        "xsrf_cookies": True,
        "cookie_secret": "2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
        "debug": True,
    }

    app = tornado.web.Application([
            (r"/", IndexHandler),
            (r"/login", LoginHandler),
            (r"/chat", ChatHandler),
        ], **settings,)
    http_server = tornado.httpserver.HTTPServer(app)
    define("port", default=8000, type=int)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
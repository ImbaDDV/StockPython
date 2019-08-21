#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-12
# @Author: Minsk
# @Desc  : 
# @File  : server_test.py
# @Software : PyCharm

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            # 创建一个字典
            mydict = {}
            mydict['filename'] = '2019-07-12_9-05-10.png'
            mydict['filedata'] = data
            # 将字典转换成json
            json_str = dumps(mydict)
            # 将json发送给客户端
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 绑定IP地址和端口（区分不同的服务）
    server.bind(('127.0.0.1', 6789))
    # 开启监听-监听客户端到服务端的请求
    server.listen(512)
    print('服务器开始监听。。。')
    # 将二进制数据处理成base64再解码成字符串
    with open('F:/2019-07-12_9-05-10.png', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        # 过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        # 创建线程返回json数据
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()

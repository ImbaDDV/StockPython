#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-12
# @Author: Minsk
# @Desc  : 
# @File  : client_test.py
# @Software : PyCharm

from socket import socket
from base64 import b64decode
from json import loads


def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要指定IP地址和端口)
    client.connect(('127.0.0.1', 6789))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 3.从服务器接收数据,由于不知道数据大小，每次接受1024字节
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    # 将接收到的二进制数据解码转换成json数据并换成字典
    mydict = loads(in_data.decode('utf-8'))

    filename = mydict['filename']
    filedata = mydict['filedata'].encode('utf-8')
    with open('H:/'+filename,'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存.')


if __name__ == '__main__':
    main()
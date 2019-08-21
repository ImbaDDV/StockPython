# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-11
# @Author: Minsk
# @Desc  : 
# @File  : weixin.py
# @Software : PyCharm

import itchat


def main():
    # 登录
    itchat.login()
    # 发送消息
    itchat.send(u'你好', 'filehelper')


if __name__ == '__main__':
    main()

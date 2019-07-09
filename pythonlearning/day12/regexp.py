#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-8
# @Author: Minsk
# @Desc  : 验证输入用户名和QQ号是否有效并给出对应的提示信息。
# @File  : regexp.py
# @Software : PyCharm


import re

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""


def main():
    username = input('请输入用户名：')
    qq = input('请输入QQ：')
    # 正则表达式时使用了“原始字符串”的写法（在字符串前面加上了r）
    # 用正则表达式判断用户名是否正确
    # m1 = re.match(r'^[0-9a-zA-Z]{6,20}$',username)
    m1 = re.match(r'^\w{6,20}$', username)
    # 用正则表达式判断QQ号是否正确
    m2 = re.match(r'^[1-9]\d{4-11}$', qq)
    if not m1:
        print('用户名不符合要求')
    if not m2:
        print('QQ号不符合要求')


if __name__ == '__main__':
    main()

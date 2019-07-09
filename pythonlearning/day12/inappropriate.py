#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-9
# @Author: Minsk
# @Desc  : 替换字符串中的不良内容
# @File  : inappropriate.py
# @Software : PyCharm

import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    # flags参数可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等,多个匹配要求时，可使用|,例如flags=re.I | re.M
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()

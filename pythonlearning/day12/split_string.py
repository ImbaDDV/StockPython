#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-9
# @Author: Minsk
# @Desc  : 拆分长字符串
# @File  : split_string.py
# @Software : PyCharm

import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    main()

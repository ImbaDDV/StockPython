#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-21
# @Author: Minsk
# @Desc  : 
# @File  : itertools_test.py
# @Software : PyCharm

import itertools


def main():
    print(itertools.permutations('ABCD'))
    print(itertools.combinations('ABCDE', 3))
    print(itertools.product('ABCD', '123'))

if __name__ == '__main__':
    main()

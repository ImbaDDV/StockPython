#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-21
# @Author: Minsk
# @Desc  : 
# @File  : collections_test.py
# @Software : PyCharm

from collections import Counter


def main():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(1))


if __name__ == '__main__':
    main()

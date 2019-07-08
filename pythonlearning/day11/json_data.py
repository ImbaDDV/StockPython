#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-8 10:51
# @Author : Minsk
# @Site : 
# @File : json_data.py
# @Software: PyCharm

import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    """
    将字符串的内容反序列化成字典
    mystr = '{"name": "石巍"}' 
    print(json.loads(mystr))
    """
    try:
        # 创建data.json文件，编码utf-8给予写权限
        with open('data.json', 'w', encoding='utf-8') as fs:
            # 将mydict内容写入文件中
            json.dump(mydict, fs)
        # 读data.json文件
        with open('data.json', 'r', encoding='utf-8') as fs:
            # 将文件中的json数据写入到列表中
            json.dumps(mydict)
            # 将文件中的JSON数据反序列化成对象
            mydict = json.load(fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')
    print(mydict)


if __name__ == '__main__':
    main()

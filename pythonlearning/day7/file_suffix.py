# @Author: Shi Wei
# @Date:   2019-07-02
# @Email:  250110242@qq.com
# @Project: Demo
# @Last modified by:   Shi Wei
# @Last modified time: 2019-07-02

"""
练习3：设计一个函数返回给定文件名的后缀名
"""
import os

def get_suffix(filename,has_dot=False):

    # 返回的后缀是否需要带点
    # 查找.的位置
    pos = filename.rfind('.')
    # 判断文件名称是否正确
    if 0 < pos < len(filename):
        # 是否需要带点
        index = pos if has_dot else pos + 1
        return  filename[index:]

if __name__ == '__main__':
    print(get_suffix('file.py',True))

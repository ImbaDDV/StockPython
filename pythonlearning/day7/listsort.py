# @Author: Shi Wei
# @Date:   2019-07-02
# @Email:  250110242@qq.com
# @Project: Demo
# @Last modified by:   Shi Wei
# @Last modified time: 2019-07-03

"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""

def list_sort(list):
    list.sort(reverse=True)
    return list

if __name__ == '__main__':
    list = [2,1,3]
    list_sort(list)
    print('最大元素：%d' % list_sort(list)[0])
    print('第二大元素：%d' % list_sort(list)[1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-19
# @Author: Minsk
# @Desc  : 
# @File  : sort_test.py
# @Software : PyCharm
import random
import timeit
from functools import wraps
from time import time

# 无参数的装饰器
# def record_time(func):
#     """自定义装饰函数的装饰器"""
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         return result
#
#     return wrapper

# 有参数的装饰器
# def record_time(output):
#     """自定义带参数的装饰器"""
#
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             output(func.__name__, time() - start)
#             return result
#
#         return wrapper
#
#     return decorate

class Record():
    """自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper

@Record
def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


# @record_time
def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """高质量冒泡排序(搅拌排序)"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


# @record_time
def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def fuction_time(f, origin_items):
    start = timeit.default_timer()
    f(origin_items)
    end = timeit.default_timer()
    return end - start


def main():
    origin_items = [random.randint(1, 1000) for x in range(1, 1000)]
    select_sort(origin_items)
    bubble_sort(origin_items)
    merge_sort(origin_items)
    quick_sort(origin_items)
    # print(fuction_time(select_sort, origin_items))
    # print(fuction_time(bubble_sort, origin_items))
    # print(fuction_time(merge_sort, origin_items))
    # print(fuction_time(quick_sort, origin_items))
    # prices = {
    #     'AAPL': 191.88,
    #     'GOOG': 1186.96,
    #     'IBM': 149.24,
    #     'ORCL': 48.44,
    #     'ACN': 166.89,
    #     'FB': 208.09,
    #     'SYMC': 21.29
    # }
    # # 用股票价格大于100元的股票构造一个新的字典
    # prices2 = {key: value for key, value in prices.items() if value > 100}
    # print(prices2)


if __name__ == '__main__':
    main()

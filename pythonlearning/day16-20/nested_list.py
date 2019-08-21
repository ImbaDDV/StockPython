#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-7-21
# @Author: Minsk
# @Desc  : 
# @File  : nested_list.py
# @Software : PyCharm

# def main():
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     courses = ['语文', '数学', '英语']
#     # 录入五个学生三门课程的成绩
#     # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
#     # scores = [[None] * len(courses)] * len(names)
#     scores = [[None] * len(courses) for _ in range(len(names))]
#     for row, name in enumerate(names):
#         for col, course in enumerate(courses):
#             scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#             print(scores)
#
# if __name__ == '__main__':
#     main()

def main():
    items = list(map(int, input().split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(overall[0])


if __name__ == '__main__':
    main()
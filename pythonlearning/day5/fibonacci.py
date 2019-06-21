"""
# @Author: Shi Wei <Minsk>
# @Date:   2019-06-21
# @Email:  250110242@qq.com
# @Project: 输出斐波那契数列的前20个数
#           1 1 2 3 5 8 13 21 ...
# @Last modified by:   Minsk
# @Last modified time: 2019-06-21
"""

a = 0
b = 1
for i in range(1,20):
    a, b = b, a + b
    print(a, end=' ')

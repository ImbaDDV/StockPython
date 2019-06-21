# @Author: Shi Wei <Minsk>
# @Date:   2019-06-21T13:21:26+08:00
# @Email:  250110242@qq.com
# @Project: 找出1~9999之间的所有完美数
#           完美数是除自身外其他所有因子的和正好等于这个数本身的数
#           例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
# @Last modified by:   Minsk
# @Last modified time: 2019-06-21


# for num in range(1,9999):
#     sum = 0
#     for i in range(num-1, 0, -1):
#         if num % i == 0:
#             sum = sum + i
#     if sum == num:
#         print(num)

import time
import math

for num in range(28, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)

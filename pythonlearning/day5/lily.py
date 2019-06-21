# @Author: Shi Wei <Minsk>
# @Date:   2019-06-21T11:41:12+08:00
# @Email:  250110242@qq.com
# @Project: 找出100~999之间的所有水仙花数
#           水仙花数是各位立方和等于这个数本身的数
# @Last modified by:   Minsk
# @Last modified time: 2019-06-21T13:20:28+08:00


# write by Minsk
for x in range(1,9):
    for y in range(0,9):
        for z in range(0,9):
            if pow(x,3)+pow(y,3)+pow(z,3) == x*100+y*10+z:
                print(x*100+y*10+z)

# write by 骆昊
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

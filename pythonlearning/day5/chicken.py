# @Author: Shi Wei <Minsk>
# @Date:   2019-06-21
# @Email:  250110242@qq.com
# @Project: 求解《百钱百鸡》问题
#           1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
#           问公鸡 母鸡 小鸡各有多少只
# @Last modified by:   Minsk
# @Last modified time: 2019-06-21

for x in range(0,20):
    for y in range(0,33):
        for z in range(0,300):
            if x + y + z == 100 and 15*x + 9*y + z == 300:
                print('公鸡为%d,母鸡为%d,小鸡为%d' % (x,y,z))


for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

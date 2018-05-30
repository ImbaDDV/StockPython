# filer：函数filter有两个参数，一个是函数，一个是Iterable,filer是将传入的函数一次作用于每个元素，然后根据返回值是True或者False决定保留还是丢弃该元素。
# 用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。
# 先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
# 素数主函数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# 先构造一个自然数序列
def _natural_num():
    n = 1
    while True:
        yield n
        n = n + 1
# 定义筛选函数
def _not_divisible(n):
    strA = str(n)
    strB = strA[::-1]
    if int(strA) == int(strB):
        return True
    else:
        return False

def main():
    num = _natural_num()
    while True:
        num = filter(_not_divisible,num)
        n = next(num)
        yield n
        # num = filter(_not_divisible,num)

for n in main():
    if n < 200:
        print(n)
    else:
        break

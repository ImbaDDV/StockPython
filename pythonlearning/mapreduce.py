from functools import reduce
# map:函数map有两个参数，一个是函数，一个是Iterable,map将函数的逻辑作用于Iterable内的每一个元素，最后返回一个Iterator.

# 计算数的平方
def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6])
print(list(r))

# 将list内元素变成字符串
s = map(str,[1,2,3,4,5,6])
print(list(s))

# reduce:函数reduce有两个参数，一个是函数，一个是Iterable,reduce函数是将函数作用在一个序列上，然后将结果再跟序列中下一个元素进行累积计算。
# 求和
def add(x,y):
    return x + y

print(reduce(add,[1,2,3,4,5,6]))


# 将序列[1, 3, 5, 7, 9]变换成整数13579
def Int2str(x,y):
    return str(x)+str(y)

print(reduce(Int2str,[1, 3, 5, 7, 9]))

# 将字符串转换成数字
def str2Int(s):
    def fn(x,y):
        return int(x) * 10 + int(y)
    return reduce(fn,s)

str2Int('13579')

# 使用lambda函数实现字符串转换成数字
def str2Intbylambda(s):
    return reduce(lambda x,y:int(x) * 10 + int(y),s)

str2Int('13579')

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def formatName(s):
    return s.capitalize()
print(list(map(formatName,['adam', 'LISA', 'barT'])))

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    n = s.index('.')
    s = s[:n] + s[n+1:]
    def char2num(x):
        return digits[x]
    return reduce(lambda x,y:x*10+y,map(char2num,s))/(10**(len(s)-n))

print(str2float('123.456'))

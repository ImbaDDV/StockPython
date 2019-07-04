
# @Author: Shi Wei <Minsk>
# @Date:   2019-06-23
# @Email:  250110242@qq.com
# @Project: 函数和模块的使用
# @Last modified by:   Shi Wei
# @Last modified time: 2019-06-27


#实现计算求最大公约数和最小公倍数的函数

def a(x,y):
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def b(x,y):
    return x * y // a(x,y)

#实现判断一个数是不是回文数的函数。

def is_palindrome(num =121):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

#实现判断一个数是不是素数的函数。
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

#写一个程序判断输入的正整数是不是回文素数。
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('不是回文素数')

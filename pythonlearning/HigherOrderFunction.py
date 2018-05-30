# 高阶函数
# 一个函数可以接收另一个函数作为参数称为高阶函数
# 自定义函数add求和的绝对值
a = 5
b = -6
def add(x,y,f):
    return f(x)+f(y)

print(add(a,b,abs))

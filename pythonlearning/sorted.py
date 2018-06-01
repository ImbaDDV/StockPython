# sorted函数：python自带的排序函数
L = [1,2,3,4,5,-6,-7,-8]
print(sorted(L))

# sorted函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted(L,key=abs))

# sorted函数也可以反向排序
print(sorted(L,key=abs,reverse=True))

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
# 请用sorted()对上述列表分别按名字排序：
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

print(sorted(L1,key=by_name))

L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 再按成绩从高到低排序：
def by_score(t):
    return t[1]

print(sorted(L2,key=by_score,reverse=True))

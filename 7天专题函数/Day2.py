'''第二天'''
'''
1.使用sum函数实现1+2+3+...+100之和
'''
print(sum(range(1, 101)))
'''
2.列表[1,2,3,4,5]请使用map()函数输出[1,4,9,16,25]
map()函数第一个参数是function，第二个参数是一般是list
'''

def fun(a):
    return a ** 2


a = [1, 2, 3, 4, 5]
res = map(fun, a)
res = [i for i in res]
print(res)
res=map(lambda x: x ** 2, a)  # 使用 lambda 匿名函数
res=[i for i in res]
print(res)
'''
3.举例说明zip()函数用法
'''
'''
zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。
同时将这些序列中并排的元素配对。
zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;
当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。
'''
a = [1, 2]
b = [3, 4]
res = [i for i in zip(a, b)]
print(res)  # => [(1, 3), (2, 4)]

a = (1, 2)
b = (3, 4)
res = [i for i in zip(a, b)]
print(res)  # => [(1, 3), (2, 4)]

a = 'hello'
b = 'world'
res = [i for i in zip(a, b)]
print(res)  # => [('h', 'w'), ('e', 'o'), ('l', 'r'), ('l', 'l'), ('o', 'd')]

# 输入长度不同的时候，zip自动以最短序列长度为准进行截取
a = [1, 2, 3]
b = [3, 4]
res=zip(a,b)
res=zip(*res)
# res = [i for i in zip(a, b)]
print(list(res))

'''
1.map函数的用法:map函数接受两个或者两个以上的参数，第一个参数为函数，
第二个参数一般是一个或者多个列表。map函数会把列表中的每个元素都调用函数，
并返回包含每次函数返回值的新列表。
2.zip函数的用法：将传入的可迭代对象中对应的元素打包成一个个元组，
然后返回这些元组组合的结果。利用zip(*要解压的变量名)形式可以解压回列表
'''
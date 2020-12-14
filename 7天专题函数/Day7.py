'''第七天'''
'''
1.求下面代码的输出结果
答：输出结果为：1
在 python 中，strings, tuples, 和 numbers 是不可更改的对象
'''
a = 1


def change(n):
    n = 5


change(a)
print(a)  # 1
'''
2.Python中help()和dir()函数的用法是什么？
答：help()和dir()这两个函数都可以从Python解释器直接访问，并用于查看内置函数的合并转储。
help()函数：help()函数用于显示文档字符串，还可以查看与模块，关键字，属性等相关的使用信息。
dir()函数：dir()函数用于显示定义的符号。
'''
class ss:
    '''
    这个类就是用来测试的
    '''
    def __init__(self):#初始化函数
        self.z=1
    def get_z(self):
        return self.z
s=ss()
print(dir())  # 不带参数的时候返回当前模块的变量
print(dir([]))  # 查看列表所拥有的方法
print(dir(ss))
print(dir(s))
print(help(ss))

'''
3.用reduce函数实现1+2+3+...+100之和
答：reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
# Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数
from functools import reduce

a = reduce(lambda x, y: x + y, range(1, 101))
print(a)
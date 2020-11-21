'''第一天的三问'''

'''
1.Python的主要特性有哪些？（easy）
答：
1.python是个解释性语言，无需编译即可运行
2.python是动态类型的，声明变量的时候无需指定变量的类型
3.python是面向对象的，支持类和继承
4.在python中，函数也是对象，这意味着可以把它赋值给变量，或者作为其他函数的返回值
5.编写python的速度可以很快，但是python的运行通常比其他语言慢。
但是python支持基于其他语言的扩展。
比如非常流行的python库numpy就是用C语言编写的。
6.python的用途十分广泛，Web应用程序，自动化脚本，科学建模，大数据应用程序等等。
它也被称为胶水语言，可以使其他语言和组件发挥出特色
'''

'''
2.列表(list)和元组(tulple)有什么区别？(normal)
答：
1.列表是可变的，可以被修改。而元组是不可修改的，可以将元组当成不可编辑的列表
2.元组的操作一般比列表快，元组存储在单个内存块中，因为其不可变，所以不需要额外的空间来存储新对象
3.列表是相同类型的数据队列，元组通常有不同类型的数据
4.列表不能作为字典的键key，但是元组可以
'''

'''
3.不使用内置的int()API,将字符串"123"转化成123
'''


# 1.最笨的方法，利用str函数把数字变成字符串判断是否相等
def method1(s):
    num = 0
    for i in s:
        for j in range(10):
            if i == str(j):
                num = num * 10 + j
    return num


s = '123'
print(s, type(method1(s)))  # 123 <class 'int'>

from functools import reduce


# 2. 使用ord函数把字符串的字符转化成ASCII编码，然后全部编码减去0的编码即为数字
def method2(s):
    # num = 0
    # for i in s:
    #     num = num * 10 + ord(i) - ord('0')
    # return num
    #  也可以把for循环变成reduce
    # lambda num,i :num*10+ord(i)-ord('0')是代表定义了一个函数，
    # 函数参数为num和i，函数体是return了num * 10 + ord(i) - ord('0')
    # reduce(函数名，要被遍历的东西，从哪里开始遍历)，函数名中要有两个参数，然后每次会将上一次迭代的结果传入到下一次中
    return reduce(lambda num, i: num * 10 + ord(i) - ord('0'), s, 0)


s = '123'
print(s, type(method2(s)))  # 123 <class 'int'>


# 3. 使用eval函数，直接计算字符串表达式
def method3(s):
    num = 0
    for i in s:
        tmp = "%s *1 " % i
        num = num * 10 + eval(tmp)
    return num


s = '123'
print(s, type(method3(s)))  # 123 <class 'int'>

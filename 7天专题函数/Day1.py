'''第一天'''
'''
1.python中的函数是什么？
答：函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段，
只有在被调用时才会执行。要在Python中定义函数，需要使用def关键字。
'''
'''
2.python2和python3的range（100）的区别
python2返回列表，python3返回迭代器，节约内存
'''
'''
3.fun(args,**kwargs)中的args,**kwargs什么意思？
答：*args 和 **kwargs主要用于函数定义。你可以将不定数量的参数传递给一个函数。
这里的不定的意思是：预先并不知道函数的使用者会传递多少个参数给你，
所以在这个场景下使用这两个关键字。
*args和**kwargs可以同时在函数的定义中,但是args必须在**kwargs前面.
*args是用来发送一个非键值对的可变参数的参数列表给一个函数。
'''
def aaa(a, *args):
    print(a)
    for i in args:
        print(i)
aaa('hi')
aaa('hi', 'hello', 'world')
'''
**kwargs允许你将不定长度的键值对作为参数传递给一个函数。
如果你想要在一个函数里处理带名字的参数，你应该使用**kwargs。
'''
def aaa(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
aaa(name='maishu', city='San Francisco')
'''
什么是函数:函数是组织好的，重复使用的实现一定功能的代码段。
python2的range函数和python3的区别:python2返回列表，python3返回迭代器省内存
函数的可变参数:*args和**kwargs,*args表示发送一个可变参数的不带键值对的参数列表，**kwargs表示不定长的参数
'''
'''第三天'''
'''
1.如何在一个函数内部修改全局变量
答：利用global在函数内声明修改全局变量
'''
val = 100
def t():
    global val
    val = 101

t()
print(val)
'''
2.说说python中的断言方法
答：assert()方法，断言成功，则程序继续执行，断言失败，则程序报错
'''
a = 10
# assert a > 10  ## => AssertionError
print('done')

'''
3.python中copy和deepcopy的区别
答：
1、复制不可变数据类型，不管copy还是deepcopy,都是同一个地址当浅复制的值是不可变对象（数值，字符串，元组）时和=“赋值”的情况一样，对象的id值与浅复制原来的值相同。
2、复制的值是可变对象（列表和字典）
浅拷贝copy有两种情况：
第一种情况：复制的对象中无复杂子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。
第二种情况：复制的对象中有复杂子对象 （例如列表中的一个子元素是一个列表）， 改变原来的值中的复杂子对象的值 ，会影响浅复制的值。
深拷贝deepcopy：完全复制独立，包括内层列表和字典
'''
import copy

a = 'hi'
b = [1, 2, 3]
c = [a, b]
# for i in c:
#     print(id(i))

print(id(b))
d = copy.copy(b)
print(id(d))
# for i in d:
#     print(id(i))
#
# e = copy.deepcopy(c)
# for i in e:
#     print(id(i))
'''
global:在函数里面取到全局变量，然后可以对全局变量进行修改
assert:断言方法，用来判断一个变量是否满足某种条件，如果断言成功则程序继续执行，否则直接报错
copy和deepcopy:对于不可改变的数据类型，比如字符串，无论是copy还是deepcopy都是和原来对象的同一个地址。但是对于可改变的数据类型，如果是简单的子对象，比如就是单纯的[1,2,3]列表，copy和deepcopy都会新开一个地址给这个列表，而且原列表的值无法再改变copy后的列表的值了。如果是复杂子对象，比如[[1,2,3],[2,3,4]],copy之后，也会有新的地址，但是改变原来的列表中的列表值，copy之后的相应的值也会被改变，但deepcopy则是完全新开一个地址，全部独立复制过去，相当于重新弄出一个一模一样的对象。
'''
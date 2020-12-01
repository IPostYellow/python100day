'''第二天'''
'''
1.函数和面向对象编程的异同
答：
相同点：都是把程序进行封装、方便重复利用，提高效率。
不同点：函数重点是用于整体调用，一般用于一段不可更改的程序。
仅仅是解决代码重用性的问题。而面向对象除了代码重用性。
还包括继承、多态等。使用上更加灵活。
'''
'''
2.Python类中的@classmethod、@staticmethod装饰方法
答：
@classmethod 类方法，至少传入一个cls（代指类本身，类似self）参数。我们不用通
过实例化类就能访问的方法。而且@classmethod 装饰的方法不能使用实例属性，
只能是类属性。它主要使用在和类进行交互，但不和其实例进行交互的函数方法上。
@staticmethod 用来修饰类的静态方法。使用在有些与类相关函数，但不使用该类
或该类的实例。如更改环境变量、修改其他类的属性等。两者最明显的区别，
classmethod 必须使用类的对象作为第一个参数，
而staticmethod则可以不传递任何参数
'''


class MyClass(object):
    def __init__(self, r):
        self.r = r

    @classmethod
    def hello(cls):  # 必须有cls参数
        print('classmethod')

    @staticmethod
    def test():  # 可以没有参数
        print('staticmethod')


'''
3.面向对象中怎么实现限制属性只读？
答：
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问
将对象私有化，通过共有方法提供一个读取数据的接口
'''
class person:
    def __init__(self, x):
        self.__age = 10  # private
    def age(self):
        return self.__age

t = person(22)
# t.__age =10
print(t.age())

class MyCls(object):
    __weight = 50
    @property
    def weight(self):
        return self.__weight

'''
一句话概括：
1.函数和类都实现了代码重用性，但是类还实现了继承多态等功能。
2.类方法(classmethod)在需要使用类对象时被使用，必须要有cls参数，而静态方法(staticmethod)是所有实例和类本身都可用的。
3.在类中的属性名称前加__可以让属性变成私有变量，只有内部可以访问私有属性，外部不能访问。
'''
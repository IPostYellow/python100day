'''第七天'''
'''
1.抽象类可以被实例化吗？
答：不可以，因为抽象类没有完整地实现，所以无法创建其实例
'''
from abc import ABCMeta, abstractmethod

class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def test(self, maxbytes=-1):
        pass

# abcObj = MyABC()  # => TypeError: Can't instantiate abstract class MyABC with abstract methods test
# print(abcObj)

'''
2.property的使用
答：
property 有两个作用
1.作为装饰器 @property 将类方法转换为类属性（只读）
'''
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   @property
   def pi(self):
       return self.__pi

circle1 = Circle(2)
print(circle1.pi)
circle1.pi=3.14159  # 出现AttributeError异常
'''
2.property 重新实现一个属性的 setter 和 getter 方法
'''
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   def get_pi(self):
       return self.__pi

   def set_pi(self, pi):
       Circle.__pi = pi

   pi = property(get_pi, set_pi)

circle1 = Circle(2)
circle1.pi = 3.14  # 设置 pi的值
print(circle1.pi)  # 访问 pi的值

'''
3.说一下Python的魔法方法
答：
魔法方法就是可以给你的类增加魔力的特殊方法，如果你的对象实现（重载）了这些方法中的某一个，
那么这个方法就会在特殊的情况下被Python所调用，你可以定义自己想要的行为，而这一切都是自动发生的，
它们经常是两个下划线包围来命名的（比如__init___,__len__),Python的魔法方法是非常强大的所以了解
其使用方法也变得尤为重要!
__init__构造器，当一个实例被创建的时候初始化的方法，但是它并不是实例化调用的第一个方法。
__new__才是实例化对象调用的第一个方法，它只取下cls参数，并把其他参数传给__init___.
___new__很少使用，但是也有它适合的场景，尤其是当类继承自一个像元祖或者字符串这样不经常改变的类型的时候。
__call__让一个类的实例像函数一样被调用
__getitem__定义获取容器中指定元素的行为，相当于self[key]
__getattr__定义当用户试图访问一个不存在属性的时候的行为。
__setattr__定义当一个属性被设置的时候的行为
__getattribute___定义当一个属性被访问的时候的行为
'''
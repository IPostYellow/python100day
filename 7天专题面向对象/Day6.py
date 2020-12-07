'''第六天'''
'''
1.什么是接口（interface）？
答：接口是面向对象中的一个重要概念，它使你可以在不定义方法的情况下声明方法。
与类不同，接口不是蓝图，因为它们不包含要执行的详细指令或操作。
任何实现接口的类都要实现接口的方法。
别的对象只要知道接口就行，不用知道具体的实现，
当改变实现时也不会影响到接口以及使用者的使用，这就是面向对象的封装的本质所在。
'''

'''
2.python如何限制实例可以添加的变量
Python作为一种动态语言，可以在类定义完成和实例化后，给类或者对象继续添加随意个
数或者任意类型的变量或方法，这是动态语言的特性
'''
def hi(self):
    print('hi')
class Test:
    pass
t1 = Test()
t2 = Test()
# 动态添加实例变量
t1.name = "maishu"
t2.age = 18
# 动态的给类添加实例方法
Test.show = hi
t1.show()
t2.show()
'''
可以使slots限制实例的变量，比如，只允许Test的实例添加name和age属性。slots定义
的属性仅对当前类的实例起作用，对继承了它的子类是不起作用的
'''
class Test:
    __slots__ = ("name", "age")
    pass

t1 = Test()
t1.name = "maishu"
#t1.gender = 1  # AttributeError: 'Test' object has no attribute 'gender'

'''
3.关于python面向对象中的元类（metaclass）
答：当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里较难理解，也是最难使用的魔术代码。一般来说，你不会碰到需要使用metaclass的情况。
'''
# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 指示使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)

'''
什么是slots:限制实例里随意添加变量的方法
一句话总结接口:只定义了功能，但是不包含任何具体实现的代码，任何继承接口的类都要实现接口的方法
什么是元类：元类是创建类或者修改类的一种类，相当于类是元类的实例
'''
'''第五天'''
'''
1.为什么要使用面向对象，面向对象的优点有哪些？
答：
面向对象使编程更加清晰，从而简化了解决复杂问题的过程
可以通过继承重用代码，从而减少冗余
数据和代码通过封装绑定在一起
面向对象允许隐藏数据，私有数据要保密
问题可以分为不同的部分，从而易于解决
多态性的概念通过允许实体具有多种形式来为程序提供灵活性
'''
'''
2.什么是多态？
多态性是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，
父对象就可以根据当前赋值给它的子对象的特性以不同的方式运作。
简单说就是一句话：允许将子类类型的指针赋值给父类类型的指针。
实现多态，有两种方式，覆盖和重载。两者的区别在于：
覆盖(重写)在运行时决定，重载是在编译时决定。并且覆盖和重载的机制不同。
例如在 Java 中，重载方法的签名必须不同于原先方法的，但对于覆盖签名必须相同。
'''


class Animal:
    def run(self):
        print('Animal running')


class Dog(Animal):
    def run(self):
        print('Dog running')


class Cat(Animal):
    def run(self):
        print('Cat running')


# 我们只需定义一个run_twice方法，如果要新加一个Animal的子类也不需要对它做任何修改
def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
run_twice(a)
d = Dog()
run_twice(d)
c = Cat()
run_twice(c)

'''
3.说说面向对象的多继承
继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能，通过多重继承，一个子类就可以同时获得多个父类的所有功能
在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Dog继承自Animal。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
比如，让Dog除了继承自Animal外，再同时继承Pet。这种设计通常称之为MixIn。MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
'''


class Animal(object):
    def __init__(self):
        self.leg = 4
    def get_leg(self):
        print("animal跑")
        return self.leg


class Pet():
    leg = 1
    def get_leg(self):
        print("我被调用了")
        return self.leg


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def get_leg(self):
        super(Dog,self).get_leg()
        print("dog跑")
        return super().get_leg()

D = Dog()
print(D.get_leg())
'''
面向对象的优点有哪些:简化问题，清晰问题，重用代码，允许隐藏数据，多态允许了实体具有多种形式的解决方法，增加灵活性。
一句话总结多态：包括重写和重载，重写是子类继承父类时对父类同名函数的重写，重载是一个类里同名函数可以用参数的不同顺序，不同类型，不同个数区分的概念
python多继承：python是支持多继承的，相同的属性按继承从左到右顺序排最左的那个为准
'''

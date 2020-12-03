'''第四天'''
'''
1.判断一个对象是什么类型，有哪些方法？
答：
type(A)可以判断出这个对象A具体是什么类，子类和父类的type不同
isinstance(A,B)可以判断该对象A是否是某个类B的实例，父类和子类的实例也会返回True
'''
class Animal(object):
    leg = 4
class Dog(Animal):
    pass
an = Animal()
dog = Dog()
print(type(an))  # => <class '__main__.Animal'>
print(type(dog))  # => <class '__main__.Dog'>
print(isinstance(an, Animal))  # => True
print(isinstance(an, Dog))  # => False
print(isinstance(dog, Animal))  # => True
print(isinstance(dog, Dog))  # => True

'''
2.什么是方法重载和方法重写？
答：重写用于继承概念下，子类继承父类需要同名的不同函数，
即可修改重写同名方法，方法的参数与返回值与父类一致
'''
class Parent:
    def say(self):
        print('this is parent')
class Child(Parent):
    def say(self):
        print('this is child')  # 重写父类的方法
'''
重载是，同一个类里，函数或者方法有相同的名称，但是参数列表不
相同（类型不同，数量不同，位置不同）的情形，
这样的同名不同参数的函数或者方法之间，互相称之为重载函数或者方法
python并不直接支持重载，但是因为python是动态语言，
方法可以接受任何类型的参数，以及支持可变参数，可以做到重载能做的事情。
'''

'''
3.说说面向对象的实例属性和类属性
答：
实例属性属于各个实例所有，互不干扰 
类属性属于类所有，所有实例共享一个属性
'''
class Animal(object):
    leg = 4  # 这种属性是类属性，归Animal类所有,类的所有实例都可以访问到
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
print(dog.leg)  # => 4
cat = Cat()
print(cat.leg)  # => 4

class Animal(object):
    leg = 4
class Dog(Animal):
    pass
class Cat(Animal):
    leg = 3  # 相同名称的实例属性将屏蔽掉类属性
dog = Dog()
print(dog.leg)  # => 4
cat = Cat()
print(cat.leg)  # => 3, 相同名称的实例属性将屏蔽掉类属性

'''
1. 判断对象的类型可以用什么方法:type()和isinstance()
2. 方法重载和重写:方法重载是一个类里，同名函数可以用不同的参数类型、参数个数、参数次序区分成多个函数
3. 类的实例属性和类属性有什么区别：实例属性由实例所拥有，类属性由整个类以及类的所有实例所拥有，如果实例中有与类属性相同名的实例属性，将覆盖掉类属性
'''
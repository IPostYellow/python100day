'''第三天'''
'''
1.面向对象的基本特征有哪些？
答：
1.抽象
2.封装
3.继承
4.多态
'''
'''
2.你能不实例化一个类而调用类里的方法吗？
答：
类的静态（static）方法可以被直接调用而不需要实例化
可以用子类去继承它从而调用父类里的方法
'''
class Test:
    @staticmethod
    def hello():
        print('hello')
Test.hello()  # 静态方法不用实例化可以直接调用
class Test1(Test):
    pass

# 通过实例化一个子类来调用
t = Test1()
t.hello()
'''
3.说说面向对象的继承和多态
答：
当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）
'''


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass
'''
对于Dog和Cat来说，Animal就是它们的父类，对于Animal来说，
Dog和Cat就是它的子类。继承最大的好处是子类获得了父类的全部功能。
由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，
就自动拥有了run()方法
'''
dog = Dog()
dog.run()  # => Animal is running...
cat = Cat()
cat.run()  # => Animal is running...

'''当然子类也可以实现自己的run方法，这就是继承的另一个好处：多态'''
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

'''在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类'''
dog = Dog()
print(isinstance(dog, Dog))  # => True
print(isinstance(dog, Animal))  # => True

'''
1.列出面向对象的几个特征：抽象、封装、继承、多态
2.什么是继承：当我们定义一个class的时候，可以从某个现有的class继承，继承后获得父类的非私有方法和属性
3.继承的好处：提高代码的复用性，让类与类之间产生了关系，给多态提供了条件
'''
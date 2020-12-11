'''第四天'''
'''
1.用lambda函数实现两个数相乘
答：
'''
f=lambda x,y :x*y
print(f(2,3))
'''
2.简述any()和all()方法
答：
any():只要迭代器中有一个元素为真就为真
all():迭代器中所有的判断项返回都是真，结果才为真
'''
all([True, True, True, True])  ## => True
all([True, True, True, False])  ## => False

any([False, False, False, False])  ## => False
any([False, False, False, True])  ## => True

'''
3.使用lambda函数对list排序foo=[-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
'''
a = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
b = sorted(a, key=lambda x: (x < 0, abs(x)))
print(b)
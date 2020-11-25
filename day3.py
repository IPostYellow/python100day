'''
第三天的三问
'''
'''
1.下面代码的输出结果是什么？(easy)
'''
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])
'''
答：输出[]，代码将输出[],不会产生IndexError错误，就像所期望的那样，
尝试用超出成员的个数的index来获取某个列表的成员。例如，
尝试获取list[10]和之后的成员，会导致IndexError。然而，尝试获取列表的切片，
开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。
这成为特别让人恶心的疑难杂症，因为运行的时候没有错误产生，导致Bug很难被追踪到。
'''

'''
2.输入年月日，判断这一天是这一年的第几天？(normal)
'''
def juge(year, mouth, day):
    m_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 0
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        for i in range(mouth - 1):
            total_day += m_days[i]
        total_day += day
        if mouth > 2:
            total_day += 1
        return total_day
    else:
        for i in range(mouth - 1):
            total_day += m_days[i]
        total_day += day
        return total_day

import datetime
def dayofyear(year, month, day):
    # 将日期转换成date类型
    date1 = datetime.date(year=year, month=month, day=day)
    # 生成一个该年份一月一号的date对象
    date2 = datetime.date(year=year, month=1, day=1)
    # 两个date相减加1得到结果
    return (date1 - date2).days + 1

'''
3.pyhton中类方法、类实例方法、静态方法有何区别？(hard)
答：类方法: 是类对象的方法，在定义时需要在上方使用 @classmethod 
进行装饰,形参为cls，表示类对象，类对象和实例对象都可调用
类实例方法: 是类实例化对象的方法,只有实例对象可以调用，
形参为self,指代对象本身;
静态方法: 是一个任意函数，在其上方使用 @staticmethod 
进行装饰，可以用对象直接调用，静态方法实际上跟该类没有太大关系
'''
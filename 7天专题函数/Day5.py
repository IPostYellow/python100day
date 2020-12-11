'''第五天'''
'''
1.利用collections库的Counter方法统计字符串每个单词出现的次数
"asdghpqgngnergheqr;'kjageqr"
'''
from collections import Counter

s = "asdghpqgngnergheqr;'kjageqr"
res = Counter(s)
print(res)
s = [1, 3, 2]
'''
2. filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
答：
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res=filter(lambda s: s % 2 == 1, a)
print([i for i in res])

'''
3.使用递归函数实现1+2+3+...+100之和
'''
def add100(n):
    if n==0:
        return 0
    else:
        return n+add100(n-1)
print(add100(100))
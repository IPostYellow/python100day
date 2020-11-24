'''
第二天的三个问
'''
'''
1.请反转字符串 "abcd"？（easy）
'''
s = "abcd"
# 运用字符串切片,[] 中三个参数用:分隔[start : end : step]
# start：表示要截取的第一个字符所在的索引（截取时包含该字符）。如果不指定，默认为 0，也就是从字符串的开头截取；
# end：表示要截取的最后一个字符所在的索引（截取时不包含该字符）。如果不指定，默认为字符串的长度；
# step：指的是从 start 索引处的字符开始，每隔 step 个距离获取一个字符，直至 end 索引出的字符。step 默认值为 1，
# 当省略该值时，最后一个冒号也可以省略。-1 表示倒序。
print(s[::-1])
'''
2.请将字典 d= {'a':23,'g':55,'i':10,'k':37}按value值进行排序(normal)
'''
d = {'a': 23, 'g': 55, 'i': 10, 'k': 37}
z = sorted(d.items(), key=lambda x: x[1])
print(z)
'''
3.Python中内置的数据结构有几种？(hard)
答：整型int、长整型long、浮点型float、复数complex
字符串str、列表list、元组tuple
字典dict、集合set
python3中没有long，只有无限精度的int
'''

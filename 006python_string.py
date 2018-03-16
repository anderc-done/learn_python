#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

var1 = 'www.google.com'

# 字符串访问
print('var1[0]:', var1[0])
print('var1[4-10]:', var1[4:10])

# 字符串更新
print("string update:", var1[:4] + 'bing' + var1[10:])

# 字符串运算符
a = 'google'
b = '.com'

print('a + b is :', a + b)
print('a * 2 is :', a * 2)
print('a[1] is :', a[1])
print('a[1-4] are :', a[1:4])

if 'l' in a:
    print('l is in a')
else:
    print('l is not in a')

if 'm' not in a:
    print('m is not in a')
else:
    print('m is in a')

print('change row \n')
print(r'change row \n')
print(R'change row \n')
print('====================================')
# 字符串格式化

print('I am %s and I am %d years old!' % ('mike', 23))
print('====================================')

# 三引号
user_string = '''
Google公司是一家美国的跨国科技企业，
业务范围涵盖互联网广告、互联网搜索、云计算等领域，
开发并提供大量基于互联网的产品与服务，
其主要利润来自于AdWords等广告服务。
TAB(\t)
换行[\n]
'''
print(user_string)
print('====================================')

# 字符串内建函数
# 将字符串的第一个字符转换为大写
user_string = 'mike'
print(user_string.capitalize())
# 返回一个指定的宽度居中的字符串，其余部分填充字符，默认为空格
print('comments'.center(50, '='))
# 返回字符串出现的次数
user_string = 'www.google.com www google.com'
print(user_string.count('goo'))
# 检查字符串是否以*结束
user_string = 'www.google.com'
print(user_string.endswith('m'))
# 把字符串中的tab符号转为空格，tab符号默认空格数是8
user_string = 'www.google.com   '
print(user_string.expandtabs())
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
user_string = 'www.google.com'
print(user_string.find('google'))
print(user_string.find('bing'))
# index和find方法一样，只不过如果str不在字符串中会报异常
user_string = 'www.google.com'
# print(user_string.index('bing'))
print(user_string.index('google'))
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
user_string = 'www.hao123.com'
user_string1 = '123'
print(user_string.isalnum())
print(user_string1.isalnum())
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
user_string = 'google'
print(user_string.isalpha())
# 如果字符串只包含数字则返回 True 否则返回 False.
user_string = '123'
print(user_string.isdigit())
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
user_string = 'google'
user_string1 = 'Google'
print(user_string.islower())
print(user_string1.islower())
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
user_string = '123'
print(user_string.isnumeric())
# 如果字符串中只包含空白，则返回 True，否则返回 False.
user_string = ''
user_string1 = ' google'
print(user_string.isspace())
print(user_string1.isspace())
# 如果字符串是标题化的(首字母大写)则返回 True，否则返回 False
user_string = 'Google'
print(user_string.istitle())
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
user_string = 'GOOGLE'
print(user_string.isupper())
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
user_info = ['mike', 'teacher', 'shanghai']
print(','.join(user_info))
# 返回字符串长度
user_string = 'google'
print(user_string.__len__())
# 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
user_string = 'comments'
print(user_string.ljust(50, '='))
# 转换字符串中所有大写字符为小写
user_string = 'Google'
print(user_string.lower())
# 截掉字符串左边的空格或指定字符。
user_string = '   google'
print(user_string.lstrip())
user_string = '***google'
print(user_string.lstrip('*'))
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
intab = 'gole'
outtab = '1234'
trantab = str.maketrans(intab, outtab)
user_string = 'www.google.com'
print(user_string.translate(trantab))
# 返回字符串 str 中最大的字母
user_string = 'google'
print(max(user_string))
# 返回字符串 str 中最小的字母
user_string = 'google'
print(min(user_string))
# 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次
user_string = 'google google'
print(user_string.replace('go', 'ww', 1))
# rfind(str, beg=0,end=len(string))
# 类似于 find()函数，不过是从右边开始查找.

# rindex( str, beg=0, end=len(string))
# 类似于 index()，不过是从右边开始.

# rjust(width,[, fillchar])
# 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

# rstrip()
# 删除字符串字符串末尾的空格.

# split(str="", num=string.count(str))
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
user_string = "this is string example....wow!!!"
print(user_string.split())
print(user_string.split('i', 1))
print(user_string.split('w'))

# 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
user_string = "this is string example....wow!!!"
print(user_string.startswith('this'))
print(user_string.startswith('string', 8))
print(user_string.startswith('this', 2, 4))

# 在字符串上执行lstrip和rstrip
user_string = '***google**'
print(user_string.strip('*'))

# 将字符串中大写转换为小写，小写转换为大写
user_string = 'Google'
print(user_string.swapcase())

# 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
user_string = 'google'
print(user_string.title())

# translate(table, deletechars="")
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
# 见上面字符映射表

# 转换字符串中的小写字母为大写
user_string = 'google'
print(user_string.upper())

# 返回长度为 width 的字符串，原字符串右对齐，前面填充0
user_string = 'google'
print(user_string.zfill(50))

# 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false
user_string = 'google2017'
user_string1 = '23443434'
print(user_string.isdecimal())
print(user_string1.isdecimal())


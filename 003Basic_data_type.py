#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 变量赋值
counter = 100
miles = 10.1
name = "mike"

print(counter)
print(miles)
print(name)

print("============================")

a = b = c = 1
print(a)
print(b)
print(c)

print("============================")

a, b, c = 1, 1.2, "mike"
print(a)
print(b)
print(c)

print("============================")

# 数值类型

a = 20
b = 25.1
c = True
d = 1+2j
print(type(a), type(b), type(c), type(d))

# 判断a是否为int类型
a = 101
print(isinstance(a, int))

# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型

print("============================")

# 字符串
# 字符串截取
string_google = "google"

print(string_google)
print(string_google[0:-1])
print(string_google[0])
print(string_google[2:5])
print(string_google[2:])
print(string_google * 2)
print(string_google + " search")

# 向一个索引位置赋值，比如word[0] = "m"会导致错误

print("============================")

# 列表
# 列表被截取后返回一个包含所需元素的新列表
some_data = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(some_data)
print(some_data[0])
print(some_data[1: 3])
print(some_data[2:])
print(tinylist * 2)
print(some_data + tinylist)

# 列表中的元素是可以改变的
some_data[0] = "google"
some_data[2: 3] = [3.14, "mike"]
print(some_data)

print("============================")

# 元组（tuple）
# 元组的元素不能修改
some_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(some_tuple)
print(some_tuple[0])
print(some_tuple[1: 3])
print(some_tuple[2:])
print(tinytuple * 2)
print(some_tuple + tinytuple)

tuple1 = ()     # 空元组
tuple2 = (2,)   # 只含一个元素的元组
print(tuple1)
print(tuple2)

# string、list和tuple都属于sequence（序列）

print("============================")

# 集合
# 集合（set）是一个无序不重复元素的序列，基本功能是进行成员关系测试和删除重复元素
# 可以使用大括号 { } 或者 set() 函数创建集合，创建一个空集合必须用 set()
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if "Jack" in student:
    print("Jack is in this class")
else:
    print("Jack is not in this class")

# set进行集合运算

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)    # 差集
print(a | b)    # 并集
print(a & b)    # 交集
print(a ^ b)    # a和b中不同时存在的元素

print("============================")

# 字典
# 字典是无序的对象集合，字典当中的元素是通过键来存取的
# 键(key)必须使用不可变类型，在同一个字典中，键(key)必须是唯一的


tinydict = {'name': 'mike',
            'code': 1,
            'site': 'www.google.com'}

print(tinydict['name'])
print(tinydict.keys())
print(tinydict.values())

my_dictionary1 = ([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
my_dictionary2 = {x: x**2 for x in (2, 4, 6)}
my_dictionary3 = dict(Runoob=1, Google=2, Taobao=3)

# 创建空字典使用{}

print("============================")







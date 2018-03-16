#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# import

# 将整个模块（somemodule）导入，使用import
import sys
print("============python import mode===========")
print("命令行参数：")
for i in sys.argv:
    print(i)
print("\n python 路径", sys.path)

# 从某个模块中导入一个或多个函数，使用from...import

print("============python import mode===========")
from time import sleep
for i in range(3):
    print("i is :", i)
    sleep(1)

# 将某个模块中的全部函数导入，使用from somemodule import *

# 缩进
if True:
    print("True")
else:
    print("False")

# 多行语句
item_one = 1
item_two = 2
item_three = 3

total = item_one +\
        item_two +\
        item_three
print(total)

total = [item_one,
         item_two,
         item_three]
print(total)

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
print(r"this is a line with \n")

# 字符串截取
string_google = "google"

print(string_google)
print(string_google[0:-1])
print(string_google[0])
print(string_google[2:5])
print(string_google[2:])
print(string_google * 2)
print(string_google + " search")

print("------------------------")

print("hello\nrunner")
print(r"hello\nrunner")

# 等待用户输入
input("\n\n按下 Enter 键后退出")

# 同一行显示多条语句

import sys; x = "runner"; sys.stdout.write(x + " man\n")

# 多个语句构成代码组
number = 5
if number >= 5:
    print("big")
elif 2 < number < 5:
    print("middle")
else:
    print("small")

# print不换行输出
for i in range(10):
    print("x", end="")

# python可以使用 -h 参数查看各参数帮助信息

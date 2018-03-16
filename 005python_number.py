#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import math
import random

var_a = 1
del var_a
# 可以使用del删除单个或多个对象的引用
# print('var_a value is :', var_a)
print('=======================================')
# 数字类型转换
var_a = 1.0
print(int(var_a))
var_a = 1
print(float(var_a))
print('=======================================')

# 数学函数
print(abs(-10))
# ceil需要import导入,返回数字的上入整数
print(math.ceil(4.2))
# 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
x = 1
y = 2
print((x > y)-(x < y))
# 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print(math.exp(1))
# 返回数字的绝对值
print(math.fabs(-10))
# 返回数字的下舍整数
print(math.floor(4.8))
# 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print(math.log(100, 10))
# 返回以10为基数的x的对数
print(math.log10(100))
# 返回给定参数的最大值
print(max(1, 2, 5))
# 返回给定参数的最小值
print(min(1, 2, 5))
# 返回x的整数部分与小数部分，两部分的数值符号与x相同
print(math.modf(3.6))
print(math.modf(-3.2))
# 返回x**y运算后的值
print(math.pow(2, 2))
# 返回浮点数的四舍五入值，如果给出n值，代表舍入到小数点后的位数
print(round(3.345762, 3))
# 返回数字的平方根
print(math.sqrt(4))
print('=======================================')

# 随机数函数
# 需要import random
# 从序列的元素中随机挑选一个元素
temp = random.choice(range(100))
print(temp)
# 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
temp = random.randrange(20, 50, 2)
print(temp)
print('=======================================')

# 三角函数
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.tan(45))
print(math.asin(1))
print(math.acos(1))
print(math.atan(math.pi/2))
# 将弧度转换为角度
print(math.degrees(math.pi/2))
# 将角度转换为弧度
print(math.radians(90))
print(math.pi/2)
print('=======================================')

# 数学常量
print(math.pi)
print(math.e)

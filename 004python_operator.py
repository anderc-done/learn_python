#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 算术运算符
a = 21
b = 10

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print('a / b = ', a / b)
print('a % b = ', a % b)

a = 2
b = 3
print('a ** b = ', a ** b)

a = 10
b = 5
print('a // b = ', a // b)
print('=================================')

# 比较运算符
a = 10
b = 21

if a == b:
    print('1-a等于b')
else:
    print('1-a不等于b')
if a != b:
    print('2-a不等于b')
else:
    print('2-a等于b')
if a < b:
    print('3-a小于b')
else:
    print('3-a不小于b')
if a > b:
    print('4-a > b')
else:
    print('4-a不大于b')
a = 5
b = 20
if a <= b:
    print('5-a小于等于b')
else:
    print('5-a大于b')
if b >= a:
    print('6-b大于等于a')
else:
    print('6-b小于a')
print('=================================')

# 赋值运算符
a = 21
b = 10

c = a + b
print('1-c的值:', c)
c += a
print('2-c的值:', c)
c *= a
print('3-c的值:', c)
c /= a
print('4-c的值:', c)
c = 2
c %= a
print('5-c的值:', c)
c **= a
print('6-c的值', c)
c //= a
print('7-c的值', c)

print('=================================')
# 成员运算符
a = 10
b = 20
user_info = [1, 2, 3, 4, 5]
if a in user_info:
    print('1- a is in the list')
else:
    print('1- a is not in the list')

if b not in user_info:
    print('2- b is not in the list')
else:
    print('2- b is in the list')

a = 2
if a in user_info:
    print('3- a is in the list')
else:
    print('3- a is not in the list')

print('=================================')

# 身份运算符
a = 20
b = 20
if a is b:
    print('1 - a 和 b 有相同的标识')
else:
    print('1 - a 和 b 没有相同的标识')
if id(a) == id(b):
    print('2 - a 和 b 有相同的标识')
else:
    print('2 - a 和 b 没有相同的标识')
b = 30
if a is b:
    print('3 - a 和 b 有相同的标识')
else:
    print('3 - a 和 b 没有相同的标识')

if a is not b:
    print('4 - a 和 b 没有相同的标识')
else:
    print('4 - a 和 b 有相同的标识')

# is与==的区别
# is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等


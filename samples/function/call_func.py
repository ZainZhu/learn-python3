#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = abs(100)
y = abs(-20)
print(x, y)
s = set([1, 2, 3])

# 只能使用list和Tuple，不能使用set或dict作为参数
print('max(1, 2, 3) =', max([1, 2, 3]))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

def test(n):
    return n ** 2 + 1

def sum1(start, end):
    sum_for_sum = 0
    for i in range(start, end):
        sum_for_sum = sum_for_sum + test(i)
    return sum_for_sum

sum_t = sum1(1, 100)
print(sum_t)

# https://docs.python.org/3/library/functions.html#hex
n1 = 255
print(hex(n1))
n2 = 1000
print(hex(n2))

print('%#x' % n1, '%x' % n1, '%X' % n1)

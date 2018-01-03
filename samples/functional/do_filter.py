#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_odd(n):
    return n % 2 == 1


L = range(100)

print(list(filter(is_odd, L)))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 练习题：输出回数
def is_palindrome(n):
    str_n = str(n)
    len2 = int(len(str_n)/2)
    str1 = str_n[:len2]
    str2 = str_n[::-1][:len2]
    return str1 == str2


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

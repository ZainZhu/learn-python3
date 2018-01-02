#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def normalize(name):
    tmp = list(map(str.lower, name))
    tmp[0] = tmp[0].upper()
    return reduce(lambda x, y: x + y, tmp)


# def normalize(name):
#     tmp1 = name[0].upper()
#     tmp2 = name[1:].lower()
#     return tmp1 + tmp2

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(k):
    if not isinstance(k, (int, float)):
        raise TypeError('bad operand type')
    if k >= 0:
        return k
    else:
        return -k


def move(x0, y0, step, angle=0.0):
    nx = x0 + step * math.cos(angle)
    ny = y0 - step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 50, math.pi/2)
print(x, y)

# TypeError: bad operand type:
# my_abs('123')

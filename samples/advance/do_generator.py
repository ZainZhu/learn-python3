#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)


def fib(max_times):
    n, a, b = 0, 0, 1
    while n < max_times:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles():
    list_triangles = [0, 1, 0]
    while True:
        yield list_triangles[1:-1]
        current_p = list_triangles.__len__() - 1
        list_triangles.append(0)
        while current_p > 0:
            list_triangles[current_p] += list_triangles[current_p - 1]
            current_p -= 1


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

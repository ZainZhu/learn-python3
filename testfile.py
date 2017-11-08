#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

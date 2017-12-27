#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def triangles():
    list_tr = [1]
    while 1:
        yield list_tr
        list_tr = [1] + [list_tr[i] + list_tr[i + 1] for i in range(len(list_tr) - 1)] + [1]


n = 10
for t in triangles():
    print(t)
    n = n - 1
    if n < 1:
        break

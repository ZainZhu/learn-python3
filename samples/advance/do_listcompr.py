#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print("L1 is: ", L1)
print("L2 is: ", L2)

L3 = [s.lower() if isinstance(s, str) else s for s in L1]
print("L3 is: ", L3)


def f(x):
    if isinstance(x, str):
        return x.lower()
    elif x is None:
        return 0
    else:
        return x

L4 = [f(s) for s in L1]
print("L4 is: ", L4)

L5 = [s.lower() if isinstance(s, str) else 0 if s is None else s for s in L1]
print("L5 is: ", L5)


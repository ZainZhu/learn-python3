#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')


def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


add_end()
add_end()

print("%08x" % (16 * 16 - 1))


def cf(be0, af0):
    if be0 < 0 or af0 < 0:
        raise TypeError("输入成绩的范围不正确（0~100）")
    bef = float(be0)
    aff = float(af0)
    r = (aff - bef) / bef * 100
    # print(r)
    if r > 0:
        print("The results have risen: %.1f%%" % r)
    elif r == 0:
        print("No change in performance.")
    else:
        print("Results are reduced: %.1f%%" % r)
    return True


cf(85, 72)
cf(66, 72)
cf(85, 85)

students = [{"name": "Wilber", "age": 27}, {"name": "Will", "age": 28}, {"name": "June", "age": 27}]
print("name: %10s, age: %10d" % (students[0]["name"], students[0]["age"]))
print("name: %-10s, age: %-10d" % (students[1]["name"], students[1]["age"]))
print("name: %*s, age: %0*d" % (10, students[2]["name"], 10, students[2]["age"]))

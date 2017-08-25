#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Happy end
'''
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%-10s  %d' % (name, score))
    print()


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77,
    'a': 66
}

print_scores(**data)


def print_info(name, *args, **kw, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)


def print_info_all(name, master=0, *args, gender, city='Beijing', age, **kw):
    print('Personal Info')
    print('---------------')
    print('    Name: %s' % name)
    print(' Mastery: %s' % master)
    print('  Gender: %s' % gender)
    print('    City: %s' % city)
    print('     Age: %s' % age)
    print('---------------')
    print('And other:')
    print(args)
    print(kw)


print_info_all('Lisa', 72, gender='female', age=18)

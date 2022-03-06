'''
Author: fengsc
Date: 2022-03-03 18:14:13
LastEditTime: 2022-03-05 20:27:20
'''
from functools import singledispatch
li = [1, 2, 3, 4]

print(li[4:])
print(dir(list))


def func(*args):
    if len(args) == 1:
        print('one')
    elif len(args) == 2:
        print('two')
    elif len(args) == 3:
        print('three')
    else:
        print('unknown')


func(1)


@singledispatch
def func(a):
    print(f'Other: {a}')


@func.register(int)
def _(a):
    print(f'Int: {a}')


@func.register(float)
def _(a):
    print(f'Float: {a}')


func('zzz')
func(1)
func(1.2)

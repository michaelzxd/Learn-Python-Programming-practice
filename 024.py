#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


d = {'one':1, 'two':2, 'three':3}
iterable = d.keys()
iterator = iter(iterable)
print(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))

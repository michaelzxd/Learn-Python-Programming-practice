#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


def test_func():
	a = 5
	b = 6
	c = a + b
	return a, b, c
a, b, c = test_func()
print(a)
print(b)
print(c)
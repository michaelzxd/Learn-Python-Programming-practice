#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
	f = open('test.txt')
except:
	print('could not open file')
finally:
	pass

print('Program continue')
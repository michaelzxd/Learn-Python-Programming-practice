#!/usr/bin/env python3

filename = '013.py'


with open(filename, 'a') as v:
	v.write('\nI am in love')


with open(filename,'a') as v:
	v.write("\ntext.txt")

with open(filename) as f:
	content = f.readlines()

for line in content:
	print(line.rstrip())


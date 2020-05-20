#!/usr/bin/python

def takeSecond(elem):
	return elem[1]

x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=takeSecond)

print(x)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Dog:
	def __init__(self,name,size, color):
		self.name = name
		self.size = size
		self.color = color
	def bark(self):
		print('dog' + self.name + 'is barking.' )

	def run(self):
		print('dog' + self.name + 'is running.' )	

my_dog = Dog(' zzz ', 10, 'white')

n = my_dog.name
s = my_dog.size
c = my_dog.color
print("my dog's name is" + n)
print("my dog's size is " + str(s))
print("my dog's color is " + c)


my_dog.bark()
my_dog.run()



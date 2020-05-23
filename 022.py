#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import fruit
fruit.lemon()

import math
a = math.sin(90)
print(str(a))

class Dog:
	def __init__(self,name,size, color):
		self.name = name
		self.size = size
		self.color = color
	def bark(self):
		print('dog' + self.name + 'is barking.' )

	def run(self):
		print('dog' + self.name + 'is running.' )

class e_dog(Dog):
	def charge(self):
		print("Your e-dog is charged")


my_dog = e_dog(' pp ', 12, 'yellow')
print('my e-dog\'s color is ' + my_dog.color)
my_dog.charge()

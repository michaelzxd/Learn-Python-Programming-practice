#!/usr/bin/env python3

number = input('Please give a number between 1 and 10')
if int(number) < 1 or int(number) > 10:
	print('invalid nubmer')
else:
	print(number)

password = input('Please give a password')
print(f'Your password is {password}')
    	
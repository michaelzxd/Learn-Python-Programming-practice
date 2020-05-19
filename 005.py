#!/usr/bin/python

import random

num_of_numbers = 1
result = []
while num_of_numbers < 100:
	random_number = random.randrange(1,10)
	print(random_number)
	result.append(random_number)
	num_of_numbers = num_of_numbers + 1
print(result)

result_set = set(result)
for i in result_set:
	frequency_item = result.count(i)
	print(f'the frequency of item {i} is {frequency_item}')

	
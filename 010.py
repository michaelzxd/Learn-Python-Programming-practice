#!/usr/bin/python


mylist = [1,2,3,4,5]
total = 0
def sum_number():
	return sum(mylist)


print(sum_number())


states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ] 

for item in states:
	if item[0] == 'M':
		print(item)
	else:
		pass

y = [6,4,2] 
y.append(12)
print(y)

y[1] = 3
print(y)


#!/usr/bin/python

print('Today is 2/2/2016')

s = "Hello World World"
s = s.replace("World", "Universe", 1)
print(s)

s = s.replace("Hello Universe", "Hi mimi")
print(s)

a = 'PythonP'

b = a.find('P')
c = a.find('p')

print(b)
print(c)


st = ['xiaodong', 'is', 'handsome']
sentence = '_'.join(st)

print(sentence)

u = "Its to easy"
words = u.split(" ",3)
print(words)



txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)


txt2 = 'World,Earth,America,Canada'
v = ''.join(txt2.split(","))
print(v)

txt3 = "A string can b reconstructed with the join method,which combin"

q = txt3.split('\n')
print(q)







a = 1
b = 2
list1 = [3,4]
c,d = a, b
print (c, d)

e = 5
f = 6

c, *g, d = a, b, e, f

print(c,g, d)
print('-'*100)
c, *g, d = a,  f
print(c,g, d)

print('-'*100)
(c, d) = [a,  b]
print(c,d)

print('-'*100)
c, *g, d = 'Hello World'
print(c,g, d)

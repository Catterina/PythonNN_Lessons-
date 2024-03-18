import random

var1=random.random()
print((var1 * 100000 // 1 )/100)
print('-'*100)
var2 = random.randint(0,10)
print(var2)
print('-'*100)
list1=[1,2,3,4]
print(random.choice(list1))
random.shuffle(list1)
print(list1)
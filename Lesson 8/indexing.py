
var1 = 'Hello_World!'
#var1 = [10,21,32,[12,13],43,54,65,76]
# var1 = (10,21,32,43,54,65,76)

# print(var1[0])
# print(var1[3])
# print(var1[6])

# print(var1[0:5])
# print(var1[5])
# print(len(var1))
var2 = var1[:]
# var1[3][0] = 'T'
print(var1, var2, sep='\n')

var2 = var1[:5]
print(var2)

#var2 = var1[5:]
var2 = var1[5:len(var1)]
print(var2)

var2 = var1[6:11:2]
print(var2)

var2 = var1[5:0:-1]
print(var2)


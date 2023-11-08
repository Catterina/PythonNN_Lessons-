import copy
var1 = [10,21,32,[12,13],43,54,65,76]
var2 = copy.copy(var1)
var1[3][0] = 'T'
print(var1,var2, sep ='\n')

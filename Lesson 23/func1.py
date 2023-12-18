list1 =[('Karl', 100, 2000), ('Bob', 95, 2500), ('Helen', 60, 1500)]

coef = list1[0][1] * 10 * 2.2

bool_coef = coef>list1[0][2]
if bool_coef:
    print( list1[0][0], ' толстеет ')
else:
    print( list1[0][0], ' худеет ')

coef = list1[1][1] * 10 * 1.7
bool_coef = coef>list1[1][2]
if bool_coef:
    print( list1[1][0], ' толстеет ')
else:
    print( list1[1][0], ' худеет ')

coef = list1[2][1] * 10 * 1.7
bool_coef = coef>list1[2][2]
if bool_coef:
    print( list1[2][0], ' толстеет ')
else:
    print( list1[2][0], ' худеет ')

print('-'*100)

def print_thin(name, weight = 100, calories = 3000):
    coef = weight * 10 * 2.2
    bool_coef = coef < calories
    if bool_coef:
        print(name, ' толстеет при весе', weight, 'и потребляет каллорий', calories)
    else:
        print(name, ' худеет ', weight, 'и потребляет каллорий', calories)


dict1 = {'weight': 98,
         'name': 'Artem',
         'calories': 3600}

print_thin(*list1[0])
print_thin(list1[1][0], calories = list1[1][2], weight= list1[1][1] )
print_thin(list1[2][0], list1[2][1], list1[2][2])

print_thin(**dict1)


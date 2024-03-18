import itertools

print(list(itertools.product('ABCD', repeat=2)))
print('-'*100)
print(list(itertools.permutations('ABCD', 2)))
print('-'*100)
print(list(itertools.combinations('ABCD', 2)))
print('-'*100)
print(list(itertools.combinations_with_replacement('ABCD', 2)))


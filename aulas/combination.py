# Combinations, Permutations e Product - Itertools
# combinations - não importa a ordem
# permutations - importa a ordem
# product - importa a ordem e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Joana', 'Liara', 'Pedro']
camisetas = [
    ['preta', 'branca'],
    ['p', 'm'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

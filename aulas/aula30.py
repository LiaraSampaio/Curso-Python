'''
Desempacotamento + tuples

'''
nome1, *resto = ['Maria', 'Lucio', 'Pedro']
print(nome1, resto)

_, nome2, *_ = ['João', 'Liara', 'Helena']
print(nome2)

nomes = ('Maria', 'João', 'Vilma')
nomes = tuple(nomes)
print(nomes)
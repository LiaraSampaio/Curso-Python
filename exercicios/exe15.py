'''
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
#print(zipper(l1, l2))

from itertools import zip_longest #do maior pro menor

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1, l2))) #do menor pro maior
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
print()

'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores 
somados: 
Se uma lista for maior que a outra, a soma só vai considerar o tamanho
da menor.

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

'''
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
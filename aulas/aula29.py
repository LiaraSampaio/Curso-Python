# Cuidado dados mutáveis
lista_a = ['Liara', 'João', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[1] = 'MUDOU'
print(lista_a)

print(lista_b)


# for in com listas

nomes = ['Maria', 'Pedro', 'Liara']
indices = range(len(nomes))

for indice in indices:
    print(indice, nomes[indice])
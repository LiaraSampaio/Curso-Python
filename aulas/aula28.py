''''
List - Mútavel

append - Acrescenta final da lista
insert - Adiciona um intem no indice escolhido
pop - Remove o ultimo item da lista
del - Apaga um indice
clear - limpa a lista
extend - estende a lista

Create Read Update Delete
Criar  Ler  Alterar Apagar

'''
lista = [10,20,30,40]

lista[2] = 300
print(lista)

del lista[2]
print(lista)

lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

lista.pop(5)
print(lista)
ultimo_valor = lista.pop()

print(lista, 'Removido:', ultimo_valor)

lista.insert(4, 55)
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)


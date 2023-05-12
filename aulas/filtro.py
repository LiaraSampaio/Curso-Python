# lista filtre

lista = [n for n in range(10) if n < 5]
print(lista)
print()

numero = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]
print(numero)
print()

v = [1, 2, 3, 4, 5]
divisao = [n / 2 for n in v]

print(v)
print(divisao)
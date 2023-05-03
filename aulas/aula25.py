# FOR / IN
'''
Iterável = str, range
Iterador = quem sabe entregar um valor por vez
next = me entregue proximo valor
iter = me entregue seu iterador

'''
texto = 'Python'

# Para cada letra em texto
for letra in texto:
    print(letra)


# RANGE (start, stop, step)
numeros = range(0,10,2)

for numero in numeros:
    print(numero)


texto = iter('Liara')
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (A-F e 0-9)

'''
nome = 'Liara'
preco = 1000.958973
variavel = '%s, o preço é R$%.2f' % (nome,preco)

print(variavel)
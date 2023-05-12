'''
Set (Eficiente para remover valores duplicados)
set(interável) ou {1,2,3} 
    - mostra palavras separadas fora de ordem
    - não tem indices

Métodos uteis:
    - add, update, clear, discard
Operadores:
    - unir |
    - interseção & pega valor incomun
    - diferença somente no set da esquerda -
    - diferença simetrica itens q nao estao em ambos ^ 

'''
s1 = set('Liara')
s2 = {'Liara', 1, 2, 3}
s3 = {1,2,2,2,3,4}
print(s1)
print(s2)
print(s3)
print(2 not in s3)

print()

v = set()
v.add('Lili')
v.update(('Olá', 1,2))
v.discard('Olá')
print(v)

print()

x1 = {1, 2, 3}
x2 = {2, 3, 4}
x3 = x1 | x2
x4 = x1 & x2
x5 = x2 - x1
x6 = x1 ^ x2
print(x3)
print(x4)
print(x5)
print(x6)

print()

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS VOCE ACHOU A LETRA!')
        break
    print(letras)
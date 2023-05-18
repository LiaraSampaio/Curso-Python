'''
dir - define o nome dentro da string

hasattr - método retorna true se um objeto tiver o atributo 
nomeado fornecido e false se não tiver.

getattr - método retorna o valor do atributo nomeado de um objeto.
Se não for encontrado, retorna o valor padrão fornecido para a função.

Generator expression, Iterables e Iterators em Python
sys.getsizeof - pega o tamanho dos bytes

'''
import sys

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista)) # Salva tudo na memoria
print(sys.getsizeof(generator)) # nao salva tudo na memoria, vai pegando por vez, pausa

def generator(n=0):
    yield 1 #pausa
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Vou terminar...')
    return 'Acabou!'

gen = generator(n=0)
# print(next(gen)) 
# print(next(gen)) 
# print(next(gen)) 

for n in gen:
    print(n)


def gene(x=0, maximum=10):
    while True:
        yield x
        x += 1

        if x > maximum:
            return
    
g = gene(maximum=10)
for x in g:
    print(x)
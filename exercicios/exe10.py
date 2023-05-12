'''
Crie uma função que multiplica todos os argumentos
retorne o total para uma variavel e mostre o valor
da variavel.

'''
def multiplicador(*args):
    numero = 1
    for multiplica in args:
        numero *= multiplica
    return numero

multiplicao = multiplicador(5,10,30)
print(multiplicao)


'''
Crie uma função que fala se um número é par ou ímpar.

'''
def par_impar(numero):    
    multiplo_2 = numero % 2 == 0

    if multiplo_2:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(11))
print(par_impar(6))
print(par_impar(33))

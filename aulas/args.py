'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento) espalha

sum() - soma

'''

x, y, *resto = 1,2,3,4
print(x, y, resto)


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

somas = soma(2,3,5,10,9)
print(somas)
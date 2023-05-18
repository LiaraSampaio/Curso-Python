'''
Valores Truthy e Falsy
Mutáveis: [] {} set()
Imutávies: () "" 0 0.0 None False range(0,10)

'''
lista = [] # com valor é truthy
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))

'''
FUNÇÕES(def) - determina uma ação

'''
def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='sem nome'):
    print(f'Olá, {nome}!')

saudacao('Liara Bessa')
saudacao()

# Argumentos nomeados e não nomeados

def soma(x, y):
    print(f'{x=} y={y}','|', 'x + y = ', x + y)
    
soma(2, 3)
soma(y=2, x=3)


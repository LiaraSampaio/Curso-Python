# Funções decoradoras e decoradores
# Adicionar / Remover / Restringir / Alterar

def inverte_string(string):
    return string[::-1] #INVERTE

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

#invertida = inverte_string('LIARA')
invertida = inverte_string('123')
print(invertida)
print()

# ------------------------------------------------------------------------------------

def decoradora(func):     # decoradora - cria uma funçao decoradora
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res    
    return aninhada

@decoradora
def soma(x, y):
    return x + y

x_mais_y = soma(10,5)
print(x_mais_y)


'''
Higher Order Functions - Funções que podem receber e/ou retornar outras 
funções

First-Class Functions - Funções que são tratadas como outros tipos de 
dados comuns (strings, inteiros, etc...)

Closure funções que retornam outras funções

'''

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia', 'Liara')
s2 = criar_saudacao('Boa noite', 'Lucas')

print(s1())
print(s2())
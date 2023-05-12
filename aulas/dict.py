"""
Dicionários em Python - dict
chave{} e valor

"""
# pessoa = dict(nome='Lucas', sobrenome='Santana')

pessoa = {
    'nome': 'Liara',
    'sobrenome': 'Bessa',
    'idade' : 31,
    'altura' : 1.66,
    'endereços' : [
        {'rua': 'Rua C-173', 'quadra': 411},
        {'rua': 'Av C-107', 'número': 12},
    ],
}
print(pessoa, type(pessoa))
print(pessoa['altura'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
print()

# Manipulando chaves e valores em dicionários

populacao = {}

populacao['nome'] = 'Lucas Eduardo'
populacao['idade'] = 23
print(populacao)
del populacao['idade']
print(populacao)
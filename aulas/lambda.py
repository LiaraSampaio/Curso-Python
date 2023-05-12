# Função lambda
# mais rápida

lista = [
    {'nome': 'Liara', 'Sobrenome': 'Bessa'},
    {'nome': 'Aline', 'Sobrenome': 'Santana'},
    {'nome': 'Teo', 'Sobrenome': 'Fernandes'},
    {'nome': 'Celia', 'Sobrenome': 'Sousa'},
]

# def orderna(item):
#     return item['nome']

# lista.sort(key=orderna)

# for item in lista:
#     print(item)

lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)


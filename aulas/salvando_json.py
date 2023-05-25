import json

# pessoas = {
#     'nome': 'Liara',
#     'sobrenome': 'Bessa',
#     'enderecos': [
#         {'rua': 'Rua C-173', 'numero': 12},
#         {'rua': 'Quadra 411', 'numero': 55},
#     ],
#     'altura': 1.66,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoas, arquivo, ensure_ascii=False, indent=2 )

with open('aula.json', 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
# groupby = agrupar por - agrupando valores(itertools)

from itertools import groupby

alunos = [
    {'nome': 'Liara', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'C'},
    {'nome': 'Camila', 'nota': 'D'},
    {'nome': 'Mario', 'nota': 'B'},
]

alunos_agrupados = sorted(alunos, key=lambda a:a['nota'])
grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
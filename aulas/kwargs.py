# Empacotamento e Desempacotamento de dicionários
# kwargs(argumentos nomeados)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 28,
    'altura': 1.70,
}

pessoas_completa = {**pessoa, **dados_pessoa}

def argumentos_nomeados(*args, **kwargs):
    print(kwargs)


argumentos_nomeados(nome='João', peso=80)
argumentos_nomeados(**pessoas_completa)

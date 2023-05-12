# List Comprehension

lista = [numero * 2 for numero in range(10)] #multiplica de 0 até 9
print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 5,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # aumento nos precos de 5%
    for produto in produtos
]
print(*novos_produtos, sep='\n') # quebra de linhas
print()


produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'escritório',
}

# isinstance - para saber qual tipo é (str, int ou float)
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # se o valor for str letra maiuscula se nao quer o valor
    for chave, valor in produto.items()
}
print(dc)
print()

print(set(range(10)))
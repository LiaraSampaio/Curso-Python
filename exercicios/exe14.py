# Exercícios
# 1- Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# 2- Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# 3- Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 1
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in produtos
]
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

# 2 
produtos_ordenados_nome = sorted(produtos, key=lambda p: p['nome'])
print()
print(*produtos_ordenados_nome, sep='\n')

# 3
produtos_ordenados_preco = sorted(produtos, key=lambda p: p['preco'])
print()
print(*produtos_ordenados_preco, sep='\n')
# Parâmetros mutáveis em funções Python

def adiciona_clientes(nome, Lista=None):
    if Lista is None:
        Lista = []
    Lista.append(nome)
    return Lista

cliente1 = adiciona_clientes('Liara')
adiciona_clientes('Maira', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Pedro')
cliente2.append('Samara')
cliente2.append('Vinicius')
print(cliente2)
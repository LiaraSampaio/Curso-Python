'''
len - quantidade de chaves
keys - mostra com as chaves
values - mostra  os valores
items - mostra com chaves e valores
setdefault - adiciona valor se a chave existe
copy - retorna cópia rasa / deepcopy é profunda
get - obtém uma chave
pop - apaga um item
popitem - apaga o ultimo item
update - atualiza um dicionatio com outro

'''
pessoa = {
    'nome': 'Liara',
    'sobrenome': 'Bessa',
    'profissão': 'Desenvolvedora'
}

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy() # faz alterçao nos dois

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa.setdefault('idade', 0) # coloca uma certa idade como padrao
print(pessoa['idade'])

d2['c1'] = 1000
d2['l1'][1] = 999
print(d1)
print(d2)
print()

nome = pessoa.popitem()
print(nome)
print(pessoa)

pessoa.update(nome='Lucas', idade=22)
print(pessoa)
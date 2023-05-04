'''
split e join com list e str
split - divide uma string
join - uni uma string
    -strip (corta todo o espaço)
    -rstrip (corta espaço da direita)
    -lstrip (corta espaço da esquerda)

'''
frase = 'Olha só que, coisa interassante'
lista_frases = frase.split(',')
print(lista_frases)

frase_unidas = '-'.join(frase)
print(frase_unidas)

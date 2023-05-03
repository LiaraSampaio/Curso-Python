# CONTAGEM DE PALAVRAS

frase = "O Python é uma linguagem de programação multiparadigma." \
"Python foi criado por Guido van Roussum."

print(frase.count('Python'))


texto = 'Olá mundo! Estou aprendendo a linguagem Python'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(texto):
    letra_atual = texto[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = texto.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

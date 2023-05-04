'''
python mod.py (executa o modulo)
python -u (unbuffered - como se salvasse no pc)
python -m (lib mod como script)
python -c (cmd comando)
python -i mod.py (interativo com mod)

'''
lista = ['Maria', 'João', 'José', 'Xica']
for nome in lista:
    print(nome, end=' ')


# Condicional de uma linha so
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)
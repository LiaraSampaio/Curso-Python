'''
try - tentar executar o código
except - ocorreu algum erro ao tentar executar

.isdigit = nao deixa digitar string
'''
numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número!')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um número!')


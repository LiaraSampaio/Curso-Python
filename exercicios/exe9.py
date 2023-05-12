'''
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando
cada um dos valores por uma contagem regressiva começando de 10

7*10 4*9 6*8 8*7 2*6 4*5 8*4 9*3 0*2 = 
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301 *10 = 3010 % 11 = 7

Se for > 9 entao 0
se for < 9 entao 7

'''
import re # USADO SO PRA DISPENSAR QUALQUER CARACTER Q N SEJA NUMERO

cpf_enviado_usuario = re.sub(r'[^0-9]','','746.824.890-70')
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
"""
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')
'''
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando
cada um dos valores por uma contagem regressiva começando de 10

7*10 4*9 6*8 8*7 2*6 4*5 8*4 9*3 0*2 = 
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301 *10 = 3010 % 11 = 7

Se for > 9 entao 0
se for < 9 entao 7

'''
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

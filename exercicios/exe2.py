nome = "Liara Bessa"
altura = 1.66
peso = 64.80
imc = peso / (altura * altura)

# print(nome, 'tem', altura, 'm de altura, e pesa', peso ,'quilos e seu IMC é', imc)

# "f-strings - formatação"
linha1 = f'{nome} tem {altura:.2f} de altura,'
print(linha1)

linha2= f'pesa {peso:.2f} quilos e seu IMC é {imc:.2f}'
print(linha2)
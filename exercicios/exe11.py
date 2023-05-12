'''
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro.

'''

def multiplicador(multiplica):
    def multiplicar(numero):
        return numero * multiplica
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadriplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))

'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

'''

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
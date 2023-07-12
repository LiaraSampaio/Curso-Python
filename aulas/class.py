'''
class - classes são moldes para criar novos objetos
PascalCase para nomes de classes

'''
# nome = 'Liara'
# print(nome)
# print(isinstance(nome, str))

class Pessoa: #É UMA CLASSE
    def __init__(self, nome, sobrenome): # primeiro metodo
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Liara', 'Bessa') 
print(p1.nome, p1.sobrenome)


# Métodos em instâncias
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando.')

fusca = Carro('Fusca') # INSTANCE DA CLASSE
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()


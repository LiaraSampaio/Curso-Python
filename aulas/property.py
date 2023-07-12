# @property - um getter no modo Python
    # getter - obter valor
    # setter -
# Atributos que começam com 1 ou 2 underlines nao deve ser
# usados fora da classe.

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self._cor = cor

    @property
    def cor(self):
        return self.cor_tinta

    @cor.setter
    def cor(self, valor):
        print('Estou usando SETTER', valor)
        self._cor = valor

def mostrar(caneta):
    return caneta.cor

caneta = Caneta('Azul')
caneta.cor = 'Rosa'

print(caneta.cor)


    

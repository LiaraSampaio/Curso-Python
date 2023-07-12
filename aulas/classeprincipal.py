# Classe principal (Pessoa)
    # super class, base class, parent class
# Classes filhas (Cliente)
    # sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...
class Aluno(Pessoa):
    ...

c1 = Cliente('Liara', 'Bessa')
c1.falar_nome_classe()

a1 = Aluno('Pedro', 'Souza')
a1.falar_nome_classe()


# Herança Múltipla e mixins - Log -> FileLog
# Animal -> Mamífero -> Humando -> Pessoa -> Cliente
    # Cliente(Pessoa, FileLog)

# Método de classe - Classe.mro() = retorna tupla
# atributo __mro__ = retorna lista
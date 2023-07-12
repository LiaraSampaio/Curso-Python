import json

caminho_arquivo = 'aula38.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
p1 = Pessoa('João', 33)
p2 = Pessoa('Maria', 18)
p3 = Pessoa('Joana', 10)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
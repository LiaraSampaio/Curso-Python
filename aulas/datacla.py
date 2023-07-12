# dataclass fornece tudo __init__(), __repr__(), __eq__() (entre outros)
# Em resumo: dataclasses são syntax sugar para criar classes normais.

from dataclasses import asdict, astuple, dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: int

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':
    p1 = Pessoa('Liara', 'Bessa')
    print(p1)
    print(p1.nome_completo)


@dataclass(order=True)
class Aluno:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    lista = [Aluno('A', 'Z'), Aluno('B', 'Y'), Aluno('C', 'X')]
    ordenada = sorted(lista, reverse=True)
    print(ordenada)


@dataclass
class Agenda:
    nome: str
    sobrenome: int

if __name__ == '__main__':
    a1 = Agenda('Alan', 'Souza')
    print(asdict(a1))
    print(astuple(a1))
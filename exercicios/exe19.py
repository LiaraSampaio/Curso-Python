"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
    Conta (ABC)
        ContaCorrente
        ContaPoupanca
    Pessoa (ABC)
        Cliente
            Clente -> Conta
    Banco
        Banco -> Cliente
        Banco -> Conta
"""

import abc
 
class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor): ...
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO DE R$ {valor} REAIS)')
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE DE R$ {valor} REAIS)')
            return self.saldo
    
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE DE R$ {valor} REAIS)')
            return self.saldo
    
        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
   
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade  

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
     def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta : contas.Conta | None = None    
   
class Banco():
    def __init__(self, agencias: list[int] | None = None, clientes: list[int] | None = None, contas: list[int] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []        
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False
    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Liara', 31)
    cc1.conta = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    
    c2 = Cliente('João', 22)
    cp1 = contas.ContaPoupanca(110, 221, 100)
    c2.conta = cp1

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)

    
# criação da classe ContaBancaria
class ContaBancaria:
    # construtor
    def __init__(self, num_conta):
        # usamos para definir os atributos da classe
        self._saldo = 0 # tornando o saldo proto-privado
        self.titular = ""
        self.__num_conta = num_conta # hard protection

    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError("Valor não pode ser maior que o saldo")
        self._saldo -= valor

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Valor não pode ser menor que 0")
        self._saldo += valor

    @property # decorator que reflete o getter de uma propriedade
    def saldo(self):
        return self._saldo

    @property
    def num_conta(self):
        return self.__num_conta



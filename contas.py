class ContaCorrente:

    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo(self, valor):
        self.__saldo = valor

    def sacar(self, valor):
        if valor > self.__saldo:
            raise ValueError("Valor não pode ser maior do que o saldo ...")
        self.__saldo = self.__saldo - valor

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Valor de depósito não pode ser negativo")
        self.__saldo = self.__saldo + valor

    def imprimir(self):
        print(f"Núm: {self.numero}, Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")


class ContaCorrenteEspecial(ContaCorrente):

    def __init__(self, numero, titular, especial):
        super().__init__(numero, titular)
        self.__especial = especial

    @property
    def especial(self):
        return self.__especial

    @especial.setter
    def especial(self, valor):
        if self.saldo < 0:
            raise ValueError("Especial não pode ser alterado quanto está em uso")
        self.__especial = valor

    def sacar(self, valor):
        if valor > self.saldo + self.especial:
            raise ValueError("Valor não pode ser maior que o saldo conjugado com o especial")
        self._ContaCorrente__set_saldo(self.saldo - valor)

    def imprimir(self):
        super().imprimir()
        print(f"Especial: {self.especial}")


def main():
    print("----------- Conta Corrente --------------")
    cc = ContaCorrente(1234, "Janio Horácio")
    cc.depositar(150)
    cc.imprimir()
    cc.sacar(80)
    cc.imprimir()

    print("----------- Conta Corrente Especial -------------")
    ce = ContaCorrenteEspecial(3456, "Tulio Mario", 120)
    ce.depositar(100)
    ce.imprimir()
    ce.sacar(200)
    ce.imprimir()


if __name__ == "__main__":
    main()

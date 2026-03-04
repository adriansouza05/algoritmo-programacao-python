class ContaBancaria:
    def __init__(self, titular):
        self._saldo = 0
        self._titular = titular

    def sacar(self, valor):
        if valor <= 0 and valor > self._saldo:
            raise ValueError("Valor não pode ser maior que o saldo")
        self._saldo -= valor

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor não pode ser menor que 0")
        self._saldo += valor

    def exibir_saldo(self):
        return f"\nTitular: {self._titular} | Saldo: {self._saldo}"
    
conta1 = ContaBancaria("Ana")
conta2 = ContaBancaria("Bruno")

conta1.depositar(100)
conta2.depositar(200)
print(conta1.exibir_saldo())
print(conta2.exibir_saldo())

conta1.sacar(10)
conta2.sacar(10)
conta2.depositar(1000)
print(conta1.exibir_saldo())
print(conta2.exibir_saldo())
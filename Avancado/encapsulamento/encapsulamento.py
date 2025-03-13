class Conta:
    def __init__(self,nro_agencia, saldo=0):
        self._saldo = saldo # "privado mas não é impossível de ser modificado, por convensão não é alterado"
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        #...
        self._saldo += valor

    def sacar(self, valor):
        #...
        self._saldo += valor

    def mostrar_saldo(self):
        #...
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)

print(conta.mostrar_saldo())
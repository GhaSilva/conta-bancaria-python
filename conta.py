class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}" .format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo: R$ {} do titular {}" .format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __saque_autorizado(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if self.__saque_autorizado(valor):
            self.__saldo -= valor
            print("Saque feita com sucesso")
        else:
            print("Passou do limite")

    def transfere(self, valor, destino):
        destino.deposita(valor)
        self.saca(valor)

    def getSaldo(self):
        return self.__saldo

    def getTitular(self):
        return self.__titular

    def getLimite(self):
        return self.__limite

    def setLimite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

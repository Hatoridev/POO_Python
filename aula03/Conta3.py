class Conta3:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print("Titular:", self.titular)
        print("Número da conta:", self.numero)
        print("Saldo:", self.saldo)


class Conta2:
    def __init__(self, titular, numero, saldo):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo  # Inicializando o saldo diretamente aqui

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def set_saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo




print("Testando o projeto")

from Cliente2 import Cliente2
from Conta2 import Conta2

c1 = Cliente2("João", "114444-2222")
conta = Conta2(c1.get_nome(), 6565, 0)
print(conta.titular, "Numero: ", conta.numero, "Seu Saldo: ", conta.saldo)


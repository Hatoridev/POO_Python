from Cliente3 import Cliente3
from Conta3 import Conta3

c1 = Cliente3("João", "114444-2222")
conta = Conta3(c1.get_nome(), 1222)
conta.deposita(100)
conta.saque(50)
conta.extrato()


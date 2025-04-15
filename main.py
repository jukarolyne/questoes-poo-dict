from poo.clientes import Cliente
from poo.contas import Conta
from poo.bancos import Banco

elis = Cliente('Elis Anne', '40028922')
jade = Cliente('Jade Armand', '20191029')
josef = Cliente('Josef Evans', '01928320')
theresa = Cliente('Theresa Martin', '32109421')

contaEJ = Conta([elis.nome, jade.nome], [elis.telefone, jade.telefone], "060406")
contaT = Conta([theresa.nome], [theresa.telefone], "102938")
contaJE = Conta([josef.nome, elis.nome], [josef.telefone, elis.telefone], "123456")
directioner = Banco('Directioner')

directioner.abre_conta(contaT)
directioner.abre_conta(contaEJ)
directioner.abre_conta(contaJE)

contaJE.resumo()
contaJE.deposito(500)
contaJE.extrato()

contaT.resumo()
contaT.deposito(200)
contaT.saque(20)
contaT.extrato()

contaEJ.resumo()
contaEJ.deposito(100)
contaEJ.saque(30)
contaEJ.extrato()

directioner.lista_contas()
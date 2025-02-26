from poo.clientes import Cliente
from poo.contas import Conta
from poo.bancos import Banco

joao = Cliente('João Lucas', '993706929')
julia = Cliente('Júlia Karolyne', '998687041')
maria = Cliente('Maria José', '999381180')
jose = Cliente('José Klayber', '997788545')

contaJJ = Conta([joao.nome, jose.nome], [joao.telefone, jose.telefone], "060406")
contaJ = Conta([joao.nome], [joao.telefone], "102938")
contaJM = Conta([julia.nome, maria.nome], [julia.telefone, maria.telefone], "123456")
directioner = Banco('Directioner')

directioner.abre_conta(contaJ)
directioner.abre_conta(contaJM)
directioner.abre_conta(contaJJ)

contaJJ.resumo()
contaJJ.deposito(500)
contaJJ.extrato()

contaJ.resumo()
contaJ.deposito(200)
contaJ.saque(20)
contaJ.extrato()

contaJM.resumo()
contaJM.deposito(100)
contaJM.saque(30)
contaJM.extrato()

directioner.lista_contas()
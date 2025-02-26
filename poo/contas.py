class Conta:
    def __init__(self, cliente, telefone, numero, saldo=0):
        self.saldo = saldo
        self.numero = numero
        self.cliente = cliente
        self.telefone = telefone
        self.operacoes = []
        #self.deposito(saldo)
        print(f'Conta Nº{self.numero} criada com sucesso!')
    
    def resumo(self):
        clientes = ' - '.join(self.cliente)
        telefones = ' - '.join(self.telefone)
        print('-'*100)
        print(f'CC Número: {self.numero} Nome: {clientes} Telefone: {telefones} Saldo: {self.saldo:6.2f}')
        print('-'*100)
    
    def saque(self, valor):
        if self.saldo >=valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
            print(f'Saque realizado com sucesso. Seu saldo agora é de {self.saldo:6.2f} reais.')
        else:
            print(f'Seu saldo de {self.saldo:6.2f} reais é insuficiente para realizar esse saque.')

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPÓSITO', valor])
        print(f'Depósito de {valor:6.2f} reais realizado com sucesso. Seu saldo agora é de {self.saldo:6.2f} reais.')
    
    def extrato(self):
        print('='*40)
        print(f'Extrato CC Nº {self.numero}\n')
        for operacao in self.operacoes:
            print(f'{operacao[0]:10s} {operacao[1]:10.2f}')
        print(f'\n   Saldo:{self.saldo:6.2f}\n')
        print('='*40)

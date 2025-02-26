'''Considere um sistema onde os dados são
armazenados em dicionários. Nesse sistema
existe um dicionario principal e o dicionário
de backup. Cada vez que o dicionário
principal atinge tamanho 5, ele imprime os
dados na tela e apaga o seu conteúdo. Crie
um programa que insira dados em um
dicionário, realizando o backup a cada dado
e excluindo os dados do dicionário principal
quando ele atingir tamanho 5.'''

d = {}
backup = {}
ctrl = 1

while ctrl == 1:
    cpf = int(input('CPF: '))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))

    d[cpf] = {'nome': nome, 'idade': idade}
    backup[cpf] = {'nome': nome, 'idade': idade}
    
    if len(d) == 2:
        d.clear()

    q = int(input('0 - Não e 1 - Sim'))
    if q == 1:
        continue
    else:
        ctrl = 0

print(d)

for chave, valor in backup.items():
    print(f'{chave}: {valor}')
    
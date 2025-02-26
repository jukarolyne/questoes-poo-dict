'''Crie um programa que cadastre
informações de várias pessoas (nome,
idade e cpf) e depois coloque em um
dicionário. Depois remova todas as
pessoas menores de 18 anos do
dicionário e coloque em outro dicionário.'''

d = {}
ctrl = 1
while ctrl == 1:
    cpf = int(input('Digite o cpf: '))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))

    d[cpf] = {'nome': nome, 'idade': idade}

    q = int(input('Deseja adicionar mais alguém? 0 - Não, 1 - Sim'))

    if q == 1:
        continue
    else:
        ctrl = 0

for chave, valor in d.items():
    d2 = {}
    l = []
    if valor['idade'] < 18:
        d2[chave] = valor
        l.append(chave)

print(d2)

for elem in l:
    d.pop(elem)

print(d)

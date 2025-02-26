'''Crie um dicionário que é uma agenda e
coloque nele os seguintes dados: chave (cpf),
nome, idade, telefone. O programa deve ler
um número indeterminado de dados, criar a
agenda e imprimir todos os itens do dicionário no 
formato chave: nome-idade-fone.'''

d = {}
print('Bem-vindo à agenda telefônica eletrônica!')
ctrl = 1

while ctrl == 1:
    cpf = str(input('Digite seu cpf: '))
    nome = str(input('Digite seu nome: '))
    idade = str(input('Digite sua idade: '))
    fone = str(input('Digite seu telefone: '))

    d[cpf] = {'nome': nome, 'idade': idade, 'telefone': fone}

    q = int(input('Você quer agendar mais algum número? Digite 0 para NÃO e 1 para SIM.'))
    if q == 1:
        continue

    else:
        ctrl = q

for chave, valor in d.items():
    print(chave+': '+valor['nome']+'-'+valor['idade']+'-'+valor['telefone'])

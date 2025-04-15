'''Crie um dicionário d e coloque nele seus
dados: nome, idade, telefone,endereço.'''

d = {'nome': 'Elis', 'idade': 23, 'telefone': '821192038', 'endereco': {
    'rua':'central', 'bairro': 'la havre', 'cidade': 'french', 'cep': '9038000', 'número': 28}}
print('Bem-vindo(a) a consulta de dados!')

'''Usando o dicionário d criado
anteriormente, imprima seu nome.'''

print(d['nome'])

'''Crie um dicionário d e coloque nele os
dados fornecidos pelo usuário: nome,
idade, telefone,endereço.'''

d2 = {}

nome = str(input('Digite seu nome:'))
idade = str(input('Digite sua idade:'))
tel = str(input('Digite seu telefone:'))
endereco = str(input('Digite seu endereço:'))

d2['nome'] = nome
d2['idade'] = idade
d2['telefone'] = tel
d2['endereço'] = endereco

print(d2)

'''Também usando d, imprima todos os
itens do dicionário no formato chave :
valor, ordenado pela chave'''

for chave, valor in d2.items():
    print(chave+': '+valor)



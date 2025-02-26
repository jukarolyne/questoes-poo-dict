'''Faça um programa que cadastre os alunos da UFRPE. O programa deve receber o nome da pessoa, o curso e o endereço onde ela mora. Insira o endereço de forma que o endereço seja um dicionário dentro do dicionário de alunos. No endereço deve conter a rua, o número e o bairro. O programa deve permitir que o usuário atualize qualquer dado de um aluno.'''

dAlunos = {}     
def cadastrarAluno(dAlunos):
    nome = input('Nome:')
    curso = input('Curso:')
    rua = input('Rua:')
    numero = input('Número:')
    bairro = input('Bairro:')

    dAlunos[nome] = {'curso': curso,
                'endereco':{'rua': rua, 'numero': numero, 'bairro': bairro}}

    dadosAluno = f"Nome: {nome} - Curso: {dAlunos[nome]['curso']} - Rua: {dAlunos[nome]['endereco']['rua']} - Número: {dAlunos[nome]['endereco']['numero']} - Bairro: {dAlunos[nome]['endereco']['bairro']}"
    
    return print(dadosAluno)
    
def atualizarAluno(dAlunos):
    nome = input('Digite o aluno a ser atualizado:')
    dadosAluno = f"Nome: {nome} - Curso: {dAlunos[nome]['curso']} - Rua: {dAlunos[nome]['endereco']['rua']} - Número: {dAlunos[nome]['endereco']['numero']} - Bairro: {dAlunos[nome]['endereco']['bairro']}"

    print(dadosAluno)
    print('1 - nome')
    print('2 - curso')
    print('3 - endereço')
    atualiza = int(input('Digite o dado a ser atualizado:'))

    if atualiza == 1:
        nome_atual = input('Digite o nome atualizado:')
        dAlunos[nome_atual] = dAlunos.pop(nome)
    if atualiza == 2:
        dAlunos[nome]['curso']= input('Digite o curso atualizado:')
    if atualiza == 3:
        print('1 - rua')
        print('2 - numero')
        print('3 - bairro')
        partEndereco = int(input('Digite o dado do endereço a ser atualizado:'))
        if partEndereco == 1:
            dAlunos[nome]['endereco']['rua'] = input('Digite a rua atualizada:')
        if partEndereco == 2:
            dAlunos[nome]['endereco']['numero'] = input('Digite o numero atualizado:')
        if partEndereco == 3:
            dAlunos[nome]['endereco']['bairro'] = input('Digite o bairro atualizado:')

print('='*40)
print('Olá! Bem-vindo programa de cadastros de alunos da UFRPE.')

controle = 0

while controle == 0:
    print('='*40)
    print('1 - Cadastrar novo aluno')
    print('2 - atualizar dados')
    print('3 - sair do programa')
    escolha = int(input('O que você deseja fazer?'))
    print('='*40)

    if escolha == 1:
        cadastrarAluno(dAlunos)
        print('='*40)
        print('Cadastro realizado com sucesso!')
        controle = 0
    if escolha == 2:
        if dAlunos == {}:
            print('='*40)
            print('Você precisa cadastrar um aluno primeiro!')
            print('Escolha a opção 1 para cadastro.')
            print('='*40)
        else:
            atualizarAluno(dAlunos)
            print('='*40)
            print('Atualização feita com sucesso!')
        controle = 0
    if escolha == 3:
        print('Obrigado por usar nosso programa! Até a próxima.')
        controle =+1

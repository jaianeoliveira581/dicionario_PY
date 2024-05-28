#Crie um dicionário em Python com os seguintes dados de uma pessoa:
#- Nome
#- CPF
#- RG
#- Data de Nascimento
#- Gênero
#- E-mail
#- Telefone
#- Tipo sanguíneo
#- Profissão
#- Empresa

#O programa deverá exibir os dados da pessoa no console.

#Obs: o usuário deverá informar os dados da pessoa.

#dicionario
pessoa = {
    'nome':'',
    'CPF':'',
    'RG':'',
    'data de nascimento':'',
    'genero':'',
    'e-mail':'',
    'telefone':'',
    'tipo sanguineo':'',
    'profissão':'',
    'empresa':''
}

pessoa['nome'] = input('informe o nome: ')
pessoa['CPF'] = input('informe o CPF: ')
pessoa['RG'] = input('informe o RG: ')
pessoa['data de nascimento'] = input('informe a data de nascimento: ')
pessoa['genero'] = input('informe o genero: ')
pessoa['e-mail'] = input('informe o e-mail: ')
pessoa['telefone'] = input('informe o telefone: ')
pessoa['tipo sanguineo'] = input('informe o tipo sanguineo: ')
pessoa['profissão'] = input('informe o profissão: ')
pessoa['empresa'] = input('informe o empresa: ')

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
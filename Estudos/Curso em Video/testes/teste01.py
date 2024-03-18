print('TESTE')
nome = input('Digite seu nome: ')
nasc = int(input('Ano de nascimento: '))
ano = int(input('Ano atual: '))
idade = ano - nasc
print('A idade é {}'.format(idade))
print(type(idade))
print(type(nome))
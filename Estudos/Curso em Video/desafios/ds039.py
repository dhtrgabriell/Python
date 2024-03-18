from datetime import date

print('=' * 30)
print('>> Alistamento Mílitar <<')
print('=' * 30)

ano = int(input('Ano de nascimento: '))

atual = date.today().year

idade = atual - ano

print('-' * 30)

print('Idade: {}'.format(idade))
print('Ano atual: {}'.format(atual))

if idade < 18:
    d = 18 - idade
    print('Alistamento obrigatório daqui a {} anos'.format(d))
elif idade == 18:
    print('Alistamento obrigatório!')
    print('Dirija-se ao local mais próximo.')
else:
    d = idade - 18
    print('Ultrapassou o periodo de alistamento ({} anos)'.format(d))
    print('Dirija-se ao local mais próximo.')

print('-' * 30)
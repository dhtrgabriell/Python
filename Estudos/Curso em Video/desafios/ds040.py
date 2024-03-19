print('-=-'*10)
print(' '*5, 'Escola Privada', ' '*5)
print('-=-'*10)

print('')

nome = str(input('Nome do aluno(a): '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

print('')

print('-'*20)
print('Boletim:')

print('Nome: {}'.format(nome))
print('1ª: {}'.format(n1))
print('2ª: {}'.format(n2))

m = (n1 + n2) / 2
if m < 5.0:
    print('REPROVADO!')
elif m >= 5.0 and m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')

print('-'*20)
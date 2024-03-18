print('========== DESAFIO 33 ==========')
print('>> Maior e Menor Número <<')

n1 = int(input('Nº1: '))
n2 = int(input('Nº2: '))
n3 = int(input('Nº3: '))

print('-' * 32)

if n1 > n2 and n3:
    print('Maior número: {}'.format(n1))
elif n2 > n3:
    print('Maior número: {}'.format(n2))
else:
    print('Maior número: {}'.format(n3))

if n3 < n2 and n1:
    print('Menor número: {}'.format(n3))
elif n2 < n1:
    print('Menor número: {}'.format(n2))
else:
    print('Menor número: {}'.format(n1))

print('=' * 32)
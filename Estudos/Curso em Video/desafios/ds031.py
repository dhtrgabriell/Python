print('========== Desafio 31 ==========')
print('>> Rodoviária <<')

d = float(input('Distância da viagem (Km): '))

print('-' * 32)

if d > 200:
    v = d * 0.45
    print('O valor da passagem será de R${:.2f}'.format(v))
else:
    v = d * 0.50
    print('O valor da passagem será de R${:.2f}'.format(v))

print('=' * 32)
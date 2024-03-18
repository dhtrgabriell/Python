print('========== DESAFIO 29 ==========')
print('>> Multa <<')

km = float(input('Velocidade do carro (Km/h): '))

print('-' * 32)

if km > 80:
    multa = (km - 80) * 7
    print('Você ultrapassou o límite de velocidade (80km/h)')
    print('A multa será de R${:.2f}'.format(multa))
else:
    print('LIBERADO!')

print('=' * 32)
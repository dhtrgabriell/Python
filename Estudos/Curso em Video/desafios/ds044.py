p = float(input('Valor do produto: R$'))

print(' ')

print('''Forma de pagamento: 
      
      [ 0 ] À vista (-10%)
      [ 1 ] À vista no Cartão (-5%)
      [ 2 ] 2x no Cartão
      [ 3 ] 3x no Cartão
      [ 4 ] 4x no Cartão
      [ 5 ] 5x no Cartão''')

print(' ')

cond = int(input('Condição de pagamento: '))

if cond == 0:
    valor = p - p * 0.10
    print('Valor a ser pago: R${:.2f}'.format(valor))
elif cond == 1:
    valor = p - p * 0.05
    print('Valor a ser pago: R${:.2f}'.format(valor))
elif cond == 2:
    valor = p / 2
    print('2x de R${:.2f} (sem juros).'.format(valor))
elif cond == 3:
    j = p * 0.20
    valor = (p + j) / 3
    print('3x de R${:.2f} (juros de 20%)'.format(valor))
elif cond == 4:
    j = p * 0.20
    valor = (p + j) / 4
    print('4x de R${:.2f} (juros de 20%)'.format(valor))
else:
    j = p * 0.20
    valor = (p + j) / 5
    print('5x de R${:.2f} (juros de 20%)'.format(valor))
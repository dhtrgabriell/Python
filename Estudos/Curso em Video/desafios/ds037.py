num = int(input('Digite um número inteiro: '))

print('''Escolha uma das opções para a conversão: 
      [ 1 ] Converter para BINÁRIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL''')
op = int(input('=> '))

if op == 1:
    print('{} -> BINÁRIO = {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} -> OCTAL = {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} -> HEXADECIMAL = {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Reinicie o programa e tente novamente.')
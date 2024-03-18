print('========== DESAFIO 35 ==========')
print('>> Formando Triângulos <<')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

print('-' * 32)

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode fomar um triângulo')
else:
    print('Não pode formar um triângulo')

print('=' * 32)
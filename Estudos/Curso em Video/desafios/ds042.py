print('Formando Triângulos')
print('')

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

print('')

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar Triângulo')
    if l1 == l2 and l2 == l3:
        print('Tipo: EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('Tipo: ESCALENO')
    else:
        print('Tipo: ISÓSCELES')
else:
    print('Não pode formar Triângulo')
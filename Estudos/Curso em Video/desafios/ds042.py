l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar Triângulo')
    if l1 == l2 and l2 == l3:
        print('Tipo: EQUILÁTERO')
    elif l1 == l2 and l2 != l3 or l2 == l3 and l3 != l1 or l3 == l1 and l1 != l2:
        print('Tipo: ISÓSCELES')
    else:
        print('Tipo:5 ESCALENO')
else:
    print('Não pode formar Triângulo')
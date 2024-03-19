massa = float(input('Massa corporea(kg): '))
altura = float(input('Altura(m): '))

imc = massa / altura ** 2

print('Índice de Massa Corporal(IMC): {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso (Magreza)')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal (Normal)')
elif imc >= 25 and imc < 30:
    print('Sobrepeso (Acima)')
elif imc >= 30 and imc < 35:
    print('Obesidade Grau I')
elif imc >= 35 and imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')
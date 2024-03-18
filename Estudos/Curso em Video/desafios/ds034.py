print('========== DESAFIO 34 ==========')
print('>> Aumento <<')

nome = str(input('Nome do funcionário: '))
sal = float(input('Salário atual: R$'))

print('-' * 32)

if sal > 1250:
    nsal = sal + sal * 0.10
    print('Funcionário: {}'.format(nome))
    print('Novo salário: R${:.2f}'.format(nsal))
else:
    nsal = sal + sal * 0.15
    print('Funcionário: {}'.format(nome))
    print('Novo salário: R${:.2f}'.format(nsal))

print('=' * 32)
from colorama import init, Fore, Back, Style
from time import sleep

init()

print(Fore.YELLOW + '-=-' * 20 + Fore.RESET)

valor = float(input(Fore.MAGENTA + 'Valor da casa: R$' + Fore.RESET))
sal = float(input(Fore.GREEN + 'Salário: R$' + Fore.RESET))
anos = int(input(Fore.CYAN + 'Dividir em quantos anos? ' + Fore.RESET))

print(' ')

qvezes = 12 * anos
prestacao = valor / qvezes
porsal = sal * 0.30

print(Fore.YELLOW + 'PROCESSANDO...' + Fore.RESET)
print(' ')

sleep(3)

print('Para paga uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, prestacao))

print(' ')

if prestacao <= porsal:
    print(Back.GREEN,  Fore.WHITE + 'EMPRESTIMO APROVADO!' + Back.RESET, Fore.RESET)

    print(Fore.WHITE, Style.BRIGHT + '{}x de R${:.2f}'.format(qvezes, prestacao) + Fore.RESET, Style.RESET_ALL)
else:
    print(Back.RED, Fore.WHITE, Style.BRIGHT + 'EMPRESTIMO NEGADO!' + Back.RESET, Fore.RESET, Style.RESET_ALL)

    print(Fore.WHITE, Style.BRIGHT + 'Não cumpriu com os resquisitos nescessários.' + Fore.RESET, Style.RESET_ALL)

print(Fore.YELLOW + '---' * 20 + Fore.RESET)

print(Fore.LIGHTCYAN_EX + 'Obrigado pela preferência!' + Fore.RESET)

print(Fore.YELLOW + '-=-' * 20 + Fore.RESET)
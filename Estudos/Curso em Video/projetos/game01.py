from colorama import init, Fore, Back, Style
from random import randint
from time import sleep

init()

cor = {
    'reset': Fore.RESET,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'blue': Fore.BLUE,
    'cyan': Fore.CYAN,
    'magenta': Fore.MAGENTA,
    'yellow': Fore.YELLOW,
    'white': Fore.WHITE,
    'black': Fore.BLACK
}

background = {
    'reset': Back.RESET,
    'red': Back.RED,
    'green': Back.GREEN,
    'blue': Back.BLUE,
    'cyan': Back.CYAN,
    'magenta': Back.MAGENTA,
    'yellow': Back.YELLOW,
    'white': Back.WHITE,
    'black': Back.BLACK,
}

estilo = {
    'reset': Style.RESET_ALL,
    'negrito': Style.BRIGHT
}

print(cor['yellow'] + '-=-' * 20 + cor['reset'])
print(cor['cyan'], estilo['negrito'] + 'Vou pensar em um número de 0 a 5. Tente adivinhar...' + cor['reset'], estilo['reset'])
print(cor['yellow'] + '-=-' * 20 + cor['reset'])

comp = randint(0, 5)

n = int(input('Em que número eu pensei? '))
print(cor['magenta'] + 'PROCESSANDO...' + cor['reset'])
sleep(3)

if n == comp:
    print(cor['green'] + 'WINNER!' + cor['reset'], ' Você conseguiu me vencer!')
else:
    print(cor['red'] + 'DEFEAT!' + cor['reset'], ' Eu pensei no número \033[33m{}\033[m e não no \033[34m{}\033[m'.format(comp, n))

print(cor['yellow'] + '-=-' * 20 + cor['reset'])
print(cor['cyan'], estilo['negrito'] + 'Obrigado por jogar!' + cor['reset'], estilo['reset'])
print(cor['yellow'] + '-=-' * 20 + cor['reset'])
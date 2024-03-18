print('Cores no terminal')

cor = {
    'gray': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'purple': '\033[34m',
    'pink': '\033[35m',
    'blue': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[m'
}

print('{}Cinza!{}'.format(cor['gray'], cor['reset']))
print('{}Vermelho!{}'.format(cor['red'], cor['reset']))
print('{}Verde!{}'.format(cor['green'], cor['reset']))
print('{}Amarelo!{}'.format(cor['yellow'], cor['reset']))
print('{}Roxo!{}'.format(cor['purple'], cor['reset']))
print('{}Rosa!{}'.format(cor['pink'], cor['reset']))
print('{}Azul Ciano!{}'.format(cor['blue'], cor['reset']))
print('{}Branco!{}'.format(cor['white'], cor['reset']))
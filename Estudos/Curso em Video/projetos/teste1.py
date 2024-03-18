from colorama import init, Fore, Back, Style

init()

color = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'blue': Fore.BLUE,
    'reset': Fore.RESET
}

background = {
    'red': Back.RED,
    'green': Back.GREEN,
    'blue': Back.BLUE,
    'reset': Back.RESET
}

estilo = {
    'negrito': Style.BRIGHT
}

print(color['red'] + 'Vermelho' + color['reset'])
print(color['green'] + 'Verde' + color['reset'])
print(color['blue'] + 'Azul' + color['reset'])

print(background['red'] + 'Background Vermelho' + background['reset'])
print(background['green'] + 'Background Verde' + background['reset'])
print(background['blue'] + 'Background Azul' + background['reset'])

print(estilo['negrito'] + 'Negrito')
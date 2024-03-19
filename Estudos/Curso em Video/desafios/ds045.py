from time import sleep
from random import randint

print('Vamos jogar Jokenpô')

print(' ')

print('[1] Pedra [2] Papel [3] Tesoura')

print(' ')

comp = randint(1, 3)

player = int(input('=> '))

print(' ')

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(1)

print('')

if player == comp:
    print('EMPATE!')
elif player == 1 and comp == 3:
    print('PEDRA x TESOURA')
    print('Droga! Você me venceu!')
elif player == 2 and comp == 1:
    print('PAPEL x PEDRA')
    print('Droga! Você me venceu!')
elif player == 3 and comp == 2:
    print('TESOURA x PAPEL')
    print('Droga! Você me venceu!')
elif player == 3 and comp == 1:
    print('TESOURA x PEDRA')
    print('Haha! Ganhei de você!')
elif player == 1 and comp == 2:
    print('PEDRA x PAPEL')
    print('Haha! Ganhei de você!')
elif player == 2 and comp == 3:
    print('PAPEL x TESOURA')
    print('Haha! Ganhei de você!')
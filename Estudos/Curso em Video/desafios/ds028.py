from random import randint
from time import sleep

comp = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)

player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if player == comp:
    print('WINNER! Você conseguiu me vencer!')
else:
    print('DEFEAT! Eu pensei no número {} e não no {}'.format(comp, player))

print('-=-' * 20)
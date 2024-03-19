from time import sleep
from random import randint
print('============== JOKENPO =================')

print('')

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)

print('''Escolha: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

player = int(input('Sua jogada: '))

print('')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-'*15)
print('Computer: {}'.format(itens[comp]))
print('Player: {}'.format(itens[player]))
print('-=-'*15)

if comp == 0: # PEDRA
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('JOGADOR VENCEU!')
    elif player == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif comp == 1: # PAPEL
    if player == 0:
        print('COMPUTADOR VENCEU!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('JOGADOR VENCER!')
    else:
        ('JOGADA INVÁLIDA!')    
elif comp == 2: # TESOURA
    if player == 0:
        print('JOGADOR VENCEU!')
    elif player == 1:
        print('COMPUTADOR VENCEU!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')

print('-=-'*15)
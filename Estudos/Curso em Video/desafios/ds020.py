from random import shuffle
print('========== DESAFIO 020 ==========')
print('>> APRESENTAÇÃO <<')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Sequência da apresentção')
print(lista)

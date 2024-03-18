from math import radians, sin, cos, tan
print('========== DESAFIO 18 ==========')
print('>> SENO - COSSENO - TANGENTE <<')
a = int(input('Ângulo qualquer: '))
print('Seno: {:.2f}º'.format(sin(radians(a))))
print('Cosseno: {:.2f}º'.format(cos(radians(a))))
print('Tangente: {:.2f}º'.format(tan(radians(a))))

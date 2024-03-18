from math import hypot
print('========== DESAFIO 17 ==========')
print('>> TRIÂNGULO RETÂNGULO <<')
co = float(input('Cateto Oposto: '))
ca = float(input('Catetp Adjacente: '))
hip = hypot(co, ca)
print('O comprimento a Hipotenusa é igual a {:.2f}'.format(hip))

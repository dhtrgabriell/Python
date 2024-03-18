from math import hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hip = hypot(co, ca)
print('Hipotenusa: {:.2f}'.format(hip))
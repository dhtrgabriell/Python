print('========== DESAFIO 09 ==========')
m = float(input('Quantos metros: '))
km = m * 0.001
ocm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
print('{}km - {}ocm - {}dam - {}m - {:.0f}dm - {:.0f}cm - {:.0f}mm'.format(km, ocm, dam, m, dm, cm, mm))

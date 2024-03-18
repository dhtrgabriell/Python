from datetime import date
print('========== DESAFIO 32 ==========')
print('>> Ano BISSEXTO <<')

ano = int(input('Qual ano você quer analisar? (Digite 0 para analisar o ano atual) '))

print('-' * 32)

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

print('=' * 32)
print('========== DESAFIO 11 ==========')
print('>> CÂMBIO <<')
rs = float(input('Valor: R$'))
dolar = rs / 4.95
euro = rs / 5.34
franco = rs / 5.66
won = rs / 0.0037
iene = rs / 0.033
print('R${} em Dólar U${:.2f}'.format(rs, dolar))
print('R${} em Euro €{:.2f}'.format(rs, euro))
print('R${} em Franco suiço Fr{:.2f}'.format(rs, franco))
print('R${} em Won sul coreano ₩{:.2f}'.format(rs, won))
print('R${} em Iene ¥{:.2f}'.format(rs, iene))

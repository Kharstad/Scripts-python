km = float(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dias alugados: '))
vt = (km * 0.15) + (dias * 60)
print('O valor total a se pagar por {} dias alugados e {:.2f}km rodados é {:.2f}'.format(dias,km,vt))
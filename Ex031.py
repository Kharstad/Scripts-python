km = int(input('Digite os Km para calcular a passagem: '))
if km <= 200:
    print('O preço da passagem de {}km é R${:.2f}'.format(km, km * 0.50))
else:
    print('O preço da pssagem de {}km é R${:.2f}'.format(km, km * 0.45))

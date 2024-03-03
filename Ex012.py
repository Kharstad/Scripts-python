preço = float(input('Digite o preço do produto para previsualizar o desconto:R$'))
desconto = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, agora custará R${:.2f} '.format(preço, desconto))

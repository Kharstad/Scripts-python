a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b + c:
    print('É possível formar um triângulo com as retas {:.2f}, {:.2f} e {:.2f}'.format(a, b, c))
else:
    print('Não é possível formar um triângulo com as retas {:.2f}, {:.2f} e {:.2f}'.format(a, b, c))

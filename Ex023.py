num = int(input('Digite e seu numero: '))
''''print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



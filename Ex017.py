'''import math
oposto = float(input("Digite o ceteto oposto: "))
adjacente = float(input("Digite o cateto adjacente: "))
hipo = math.sqrt((oposto*oposto + adjacente*adjacente))
print("A hipotenusa do ceteto {} e do adjacente {} é : {:.2f}".format(oposto,adjacente,hipo))'''

import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa corresponde a {:.2f}'.format(hi))

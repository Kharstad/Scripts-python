'''import math
angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Do angulo {} são {} seu seno, {} seu cosseno e {} sua tangente".format(angulo, seno, cosseno, tangente))'''

import math
angulo = float(input('Digite seu ângulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

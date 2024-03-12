from random import randint
from time import sleep
NumeroDaSorte = randint(0,5)
print('-=-' * 20)
print('O Computador está pensando em um número entre 0 e 5')
print('-=-' * 20)
print('Processando...')
sleep(3)
NumeroUsuario = int(input('Qual número o PC escolheu? '))
if NumeroDaSorte == NumeroUsuario:
    print('PARABÉNS! Você acertou que foi o número {}'.format(NumeroDaSorte))
else:
    print('QUE AZAR! Você escolheu o número errado! O correto seria {}'.format(NumeroDaSorte))

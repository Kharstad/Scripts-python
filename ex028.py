import random
NumeroDaSorte = random.randrange(0,5)
NumeroUsuario = int(input('Qual número o PC escolheu número de 0 a 5? '))
if NumeroDaSorte == NumeroUsuario:
    print('PARABÉNS! Você acertou que foi o número {}'.format(NumeroDaSorte))
else:
    print('QUE AZAR! Você escolheu o número errado! O correto seria {}'.format(NumeroDaSorte))

Nome = str(input('Digite seu nome completo: '))
print('Seu nome completo com letras maíusculas é {}'.format(Nome.upper()))
print('Seu nome completo com letras minúsculas é {}'.format(Nome.lower()))
print('Seu nome completo possui {} letras'.format(len(Nome.replace(" ", ""))))
'''print('Seu nome completo possui {} letras'.format(len(Nome) - Nome.count(' ')))'''
dividido = Nome.split()
print('Seu nome {}, possui {} letras'.format(dividido[0], len(dividido[0])))

frase = 'Curso em vídeo Python'
'''print(len(frase))'''
frase = frase.replace('Python','Boooocetão')
print('Curso' in frase)
print(frase.lower().find('boooocetão'))
dividido = frase.split()
print(dividido[3])

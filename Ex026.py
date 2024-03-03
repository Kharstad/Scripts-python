As = str(input('Digite sua frase: ')).upper().strip()
print('Sua frase contém a letra A {}x vezes'.format(As.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(As.find('A')))
print('A letra A aparece pela última vez na posição {}'.format(As.rfind('A')))

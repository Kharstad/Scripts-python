nome = str(input('Digite seu nome: ')).strip()
nomeS = nome.find('Silva')
if nomeS < 0:
    print('Seu nome {} não contém Silva'.format(nome))
else:
    print('Seu nome {} contém Silva'.format(nome))

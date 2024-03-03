nome = str(input('Digite seu nome completo aqui: ')).strip()
dividido = nome.split()
print('Seu primeiro nome e último sobrenome juntos são {} {}'.format(dividido[0],dividido[-1]))


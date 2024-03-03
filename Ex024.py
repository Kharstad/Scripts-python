nome = str(input('Digite o nome da cidade: ')).strip()
cidade = nome.split()
if cidade[0] == 'Santo':
    print('A cidade {} começa com SANTO no nome '.format(nome))
else:
    print('A cidade {} não começa com SANTO no nome '.format(nome))


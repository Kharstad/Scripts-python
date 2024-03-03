num = int(input('Digite um número para descobrir se é ímpar ou par: '))
resto = num % 2
if resto == 0:
    print('{} é número par'.format(num))
else:
    print('{} é numero ímpar'.format(num))

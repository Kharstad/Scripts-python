salario = float(input('Digite o seu salário para consultar o acréscimo: '))
if salario > 1250.00:
    print('Seu salário R${:.2f} receberá 10%, sendo o total de R${:.2f}'.format(salario, salario * 1.1))
else:
    print('Seu salário R${:.2f} receberá 15%, sendo o total de R${:.2f}'.format(salario, salario * 1.15))

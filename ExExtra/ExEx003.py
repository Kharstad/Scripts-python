'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

while True:
    nome = str(input('Digite seu nome: '))
    if len(nome) < 3:
        print('ERROR! O nome deve conter 3 caracteres ou mais')
    else:
        break

while True:
    idade = int(input('Digite sua idade: '))
    if idade < 0 or idade > 150:
        print('ERROR! A idade deve ser entre 0 a 150 anos!')
    else:
        break

while True:
    salario = int(input('Digite seu salário: '))
    if salario < 0:
        print('ERROR! O salário deve ser maior que 0')
    else:
        break

while True:
    sexo = sexo = input("Digite o seu sexo ('F' feminino ou 'M' masculino): ").upper()
    if sexo not in ['F', 'M']:
        print('ERROR! F feminino ou M masculino')
    else:
        break

while True:
    estado_civil = str(input('Digite seu estado civil entre S, C, V e D: ')).upper()
    if estado_civil not in ['S', 'C', 'V', 'D']:
        print('ERROR! Escolha entre S, C, V e D')
    else:
        break

print("Informações válidas inseridas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)

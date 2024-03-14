''''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:

    nome = str(input('Defina seu nome: '))
    senha = str(input('Defina sua senha: '))
    if nome == senha:
        print('!!!O nome e a senha devem ser distintos!!!')
    else:
        break

print('Login criado com êxito!')

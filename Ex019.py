import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
alunos = [a1, a2, a3, a4]
sortido = random.choice(alunos)
print('O aluno escolhido dentre {}, {}, {} e {} foi: {}'.format(a1, a2 , a3 , a4, sortido))
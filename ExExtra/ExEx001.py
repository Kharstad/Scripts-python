"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido."""
num = int(input('Digite um número menor ou igual a 10 '))
if num > 10:
    int(input('Digite um número menor ou igual a 10 '))
elif num <= 10:
    print('Correto!')

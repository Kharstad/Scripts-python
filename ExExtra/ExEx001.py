"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
e continue pedindo até que o usuário informe um valor válido."""

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    
    if nota < 0 or nota > 10:
        print("Valor inválido. Por favor, digite uma nota entre 0 e 10.")
    else:
        break

print("Nota válida inserida:", nota)
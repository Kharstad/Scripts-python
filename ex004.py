n = input('Digite algo ')
print('O tipo primitivo do que digitou é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É numérico? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúculas? ', n.isupper())
print('Está em minúsuculas? ', n.islower())
print('Está capitalizada? ', n.istitle())

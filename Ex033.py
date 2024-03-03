num1 = int(input('Digite o número X: '))
num2 = int(input('Digite o número Y: '))
num3 = int(input('Digite o número Z: '))
if (num1 > num2) and (num1 > num3):
    print('O número {} é maior que os números {} e {}'.format(num1,num2,num3))
elif (num2 > num1) and (num2 > num3):
    print('O número {} é maior que os números {} e {}'.format(num2,num1,num3))
else:
    print('O número {} é maior que os números {} e {}'.format(num3,num1,num2))

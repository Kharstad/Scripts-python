velocidade = int(input('Digite a velocidade do veículo: '))
multa = (velocidade - 80) * 7
if velocidade >= 81:
    print('O veículo atingiu {}km/h e ultrapassou a marca de 80Km/h limites, sendo assim, foi multado em R${:.2f}'.format(velocidade, multa))
else:
    print('O veículo atingiu {}km/h e não foi multado'.format(velocidade))

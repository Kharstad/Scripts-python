h = float(input('Digite a altura da parede '))
w = float(input('Digite a largura agora '))
a = float(h*w)
l = a / 2
print('Calculando a altura de {}m e largura de {}m da parede, sua área da parede é {:.2f}m², serão necessários {:.1f}L de tinta para pintar'.format(h,w,a,l))

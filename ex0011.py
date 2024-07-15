altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('Numa parede de {}x{}, sua área é {}m'.format(altura, largura, area))
print('A quantidade de tinta nescessária para pintar a parede é {}l'.format(area/2))

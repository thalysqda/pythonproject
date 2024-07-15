distancia = float(input('Qual a distância da sua viagem? '))
curta = 0.50 * distancia
longa = 0.45 * distancia
if distancia <= 200:
    print('O preço da viagem foi de {:.2f}R$'.format(curta))
else:
    print('O preço da viagem foi de {:.2f}R$'.format(longa))

km = float(input('Qual quantidade de km percorrida pelo carro? '))
dias = int(input('Quantos dias o carro foi alugado? '))
C1 = 0.15 * km
C2 = 60 * dias
Ctotal = C1 + C2
print('O preço a pagar pelo carro com {} alugado e com {}km percorrido é de R${:.2f}'.format(dias, km, Ctotal))

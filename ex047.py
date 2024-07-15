print('Digite seis números')
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Noumero {}: '.format(c)))
    if n % 2 == 0:
        soma = n + soma
        cont += 1
print('A soma dos {} números pares é: {}'.format(cont, soma))

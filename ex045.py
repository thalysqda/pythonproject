soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
       cont = cont + 1
       soma = n + soma
print('A soma de todos os {} números é: {}'.format(cont, soma))

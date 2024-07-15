import random
lista = [0, 1, 2, 3, 4, 5]
pc = random.choice(lista)
n = int(input('Qual numero o computador pensou? '))
print('Prossescando...')
if n == pc:
    print('Voçê acertou!')
else:
    print('Voçê errou! o número que o computador pensou foi {} e o que voçê escolheu foi {}'.format(pc, n))

n = int(input('insira um número e mostre a sua tubuada:'))
for c in range(1, 10+1):
    s = n * c
    print('{} * {:2} = {}'.format(n, c, s))
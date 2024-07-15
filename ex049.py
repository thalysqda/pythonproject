n = int(input('Digite un número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end= ' ')
        tot = tot + 1
    else:
        print('\033[31m', end= ' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('{} é número primo'.format(n))
else:
    print('{} não é um numero primo')
from datetime import date
atual = date.today().year
contmenor = 0
contmaior = 0
for pess in range(1, 8):
    nasc = int(input('A {} pessoa nasceu em: '.format(pess)))
    idade = atual - nasc
    if idade < 18:
        contmenor += 1
    else:
        contmaior += 1
print('tem {} menores de idade'.format(contmenor))
print('tem {} pessoas maiores de idade'.format(contmaior))
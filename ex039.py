from datetime import date
ads = int(input('Que ano voçê nasceu? '))
anoatual = date.today().year
idade = anoatual - ads
if idade <= 9:
    print('MIRIN')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

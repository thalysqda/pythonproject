from datetime import date
adn = int(input('Qual ano voçê nasceu? '))
anoatual = date.today().year
idade = anoatual - adn
if idade < 18:
    print('Sua idade é {}. Voçê ainda vai se alistar ao serviço militar. Faltam {} anos'.format(idade, 18 - idade))
elif idade == 18:
    print('Sua idade é {}. Já está na hora de se alistar'.format(idade))
else:
    print('Sua idade é {}. Já passou do tempo de se alistar. Já passou {} anos do prazo'.format(idade, idade - 18))

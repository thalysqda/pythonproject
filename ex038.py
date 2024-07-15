nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
media = float((nota1 + nota2)/2)
if media < 5.0:
    print('Voçê esta reprovado! Sua média foi {:.1f}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Voçê está de recuperação. Sua média foi {:.1f}'.format(media))
else:
    print('Voçê está aprovado. Sua média foi {}'.format(media))

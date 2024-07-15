peso = float(input('Qual seu peso? kg'))
altura = float(input('Qual sua altura? '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Voçê está abaixo do peso. Seu imc é de {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Voçê está no peso ideal. Seu imc é de {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Voçê está sobrepeso. Seu imc é de {:.1f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Voçê está obeso. Seu imc é de {:.1f}'.format(imc))
else:
    print('Voçê está com obesidade mórbita. Seu imc é de {:.1f}'.format)

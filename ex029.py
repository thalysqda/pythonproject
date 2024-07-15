v = float(input('Qual a velocidade do carro em km/h: '))
if v > 80:
    m = v - 80
    p = m * 7
    print('Voçê ultrapassou a velocidade de 80km/h e foi multado! A multa vai custar {:.2f}R$'.format(p))
print("Tenha um bom dia! Diriga com cuidado")
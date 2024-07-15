salario = float(input('Qual o valor do seu sálario? R$'))
if salario < 1250:
    aumento1 = salario + (0.15 * salario)
    print('Seu sálario com aumenro de 15% é de R${:.2f}'.format(aumento1))
else:
    aumento2 = salario + (0.10 * salario)
    print('Seu sálario com aumento de 10% é de R${:.2f}'.format(aumento2))

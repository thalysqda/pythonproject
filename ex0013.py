salario = float(input('Qual o valor do seu salário? R$'))
x = 15/100 * salario
aumento = x + salario
print('Seu salário de R${:.2f} com aumento de 15% ficou com o valor de R${:.2f}'.format(salario, aumento))

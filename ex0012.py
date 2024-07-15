valor = float(input('Qual p preço do produto: R$'))
x = 0.05 * valor
desconto = valor - x
print('O novo preço do produto com desconto de 5% é de R${:.2f}'.format(desconto))

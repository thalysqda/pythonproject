preco = float(input('Qual o preço do produto R$'))
print('Condições de pagamento: \n[1] á vista dinheiro/cheque \n[2] á vista no cartão \n[3] em até 2x no cartão \n[4] 3x ou mais no cartão')
condicao = int(input('Qual condição de pagamento voçê escolhe? '))
if condicao == 1:
      desconto = 0.10 * preco
      print('O produto com desconto de 10% ficou com o valor de {:.2f}R$'.format(preco - desconto) )
elif condicao == 2:
      desconto = 0.5 * preco
      print('O produto com desconto de 5% fica com valor de {:.2f}R$'.format(preco - desconto))
elif condicao == 3:
      print('O produto fica com o preço de {:.2ff}RS'.format(preco))
elif condicao == 4:
      juros = 0.20 * preco
      print('O produto com juros de 20% fica com preço de {:.2f}R$'.format(preco + juros))

casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
ano = int(input('Quantos anos vai pagar? '))
taxa = 0.3 * salario
prestacao = (casa / ano) / 12
print('Para pagar uma casa de {:.2f}R$ em {} anos, a prestação vai ser de {:.2f}R$'.format(casa, ano, prestacao))
if prestacao > taxa:
    print('Emprestimo negado')
else:
    print('Emprestimo validado')
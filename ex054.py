soma = 0
media = 0
maioridade = 0
homevelho = ''
mulhernova = 0
for p in range(1, 5):
    print('PESSOA {}'.format(p))
    nome = str(input('Nome da priemeira pessoa: '))
    idade = int(input('Idade da primeira pessoa: '))
    sexo = str(input('Sexo da primeira pessoa: ')).upper()
    soma += idade
    if p == 1 and sexo in 'M!m':
        maioridade = idade
        homevelho = nome
    if sexo in 'M!m' and idade > maioridade:
        maioridade = idade
        homevelho = nome
    if sexo in 'F!f' and idade < 20:
        mulhernova += 1

media = (soma)/4
print('A média de idade foi: {}'.format(media))
print('O homen mais velho foi {} com idade de {}'.format(homevelho, maioridade))
print('Tem {} mulheres abaixo de 20 anos'.format(mulhernova))
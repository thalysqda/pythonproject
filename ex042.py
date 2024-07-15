import random
print('''Suas opções:
[0] pedra
[1] papel
[2] tesoura''')
itens = ('pedra', 'papel', 'tesoura')
computador = random.randint(0, 2)
jogador = int(input("Escolha uma das opções de 0 a 2:"))
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Computador inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('jogada inválida')

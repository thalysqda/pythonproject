frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
print('A frase q voce digitou foi: {}'.format(junto))
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase {} é um palindromo'.format(frase))

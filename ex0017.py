import math
co = float(input('Qual é o valor do cateto opsto? '))
ca = float(input('Qual é o valor do cateto adjascente? '))
hp = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hp))

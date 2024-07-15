import math
angulo = float(input('Qual o valor do ângulo? '))
sen = math.sin(math.radians(angulo))
print('O ângulo de {} tem um seno de {:.2f}'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O ângulo de {} tem um cosseno de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem uma tangente de {:.2f}'.format(angulo, tan))

# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE O VALOR DO SENO, COSSENO E TANGENTE

import math

ang = math.radians(float(input('Digite um ângulo qualquer:')))

sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}' .format(cos))
print('Tangente: {:.2f}'.format(tan))

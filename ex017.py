# FAÇA UM PROGRAMA QUE LEIA A MEDIDA DO CATETO ADJACENTE E DO CATETO OPOSTO DE UM TRIÂNGULO RETÂNGULO E
# CALCULE SUA HIPOTENUSA

import math

adj = float(input('Digite a medida do cateto adjecente: '))
opo = float(input('Digite a medida do cateto oposto: '))

hip = math.hypot(adj, opo)

print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hip))

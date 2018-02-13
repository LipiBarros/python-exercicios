# FACA UM PROGRAMA QUE LEIA A ALTURA E LARGURA DE UMA PAREDE EM METROS, CALCULE SUA ÁREA E INFORME QUANTOS LITROS
# DE TINTA SERÃO NECESSÁRIOS PARA PINTAR A PAREDE, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS

h = float(input('Qual a altura da parede em metros ? '))
l = float(input('Qual a largura da parede em metros ? '))

k = 2
area = l * h
lt = area / k

print('Para pintar uma parede de {:.3f} metros quadrados de área, '.format(area), end='')
print('serão necessários {:.4f} litros de tinta.' .format(lt))

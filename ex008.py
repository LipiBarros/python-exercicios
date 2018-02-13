# FAÇA UM PROGRAMA QUE LEIA UMA MEDIDA EM METROS E EXIBA O VALOR DELA EM CENTÍMETROS E MILÉMETROS

m = float(input('Digite uma medida em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('Valor em metros: {}m, corresponde a:' .format(m))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))

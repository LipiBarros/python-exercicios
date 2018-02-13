# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM Km.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR Km PARA VIAGENS DE ATÉ 200 Km
# E R$ 0,45 PARA VIAGENS MAIS LONGAS.

dist = float(input('Qual a distância da sua viagem em Km ? '))

if dist <= 200:
    val = dist * 0.50
else:
    val = dist * 0.45

print('Para a sua viagem de {} Km, o valor da passagem é de R${:.2f} reais.' .format(dist, val))

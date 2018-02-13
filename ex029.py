# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80 Km/h, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA Km ACIMA DO LIMITE.

v = float(input('Entre com a velocidade do carro: '))

if v > 80:
    multa = (v - 80) * 7.00
    print('Você foi multado e deverá pagar R${:.2f} reais de multa!!!' .format(multa))
else:
    print('Velocidade dentro do limite!!!')

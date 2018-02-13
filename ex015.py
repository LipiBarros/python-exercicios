# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS
# QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.

dias = int(input('Quantos dias o carro foi alugado ?'))
km = float(input('Quantos Km foram rodadados ?'))

valor = (dias * 60) + (km * 0.15)

print('O valor total do aluguel do carro é de R${:.2f}' .format(valor))

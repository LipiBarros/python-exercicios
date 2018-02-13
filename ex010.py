# FACA UM PROGRAMA QUE LEIA QUANTOS REAIS UMA PESSOA TEM NA CARTEIRA E INFORME O VALOR EM DÓLAR
# CONSIDERAR US$1,00 = R$3,27

grana = float(input('Quantos reais você tem na carteira ? R$'))

cotacao = 3.27

dolar = grana / cotacao

print('Com o valor de R${:.2f} reais, você pode comprar US${:.2f} dólares!' .format(grana, dolar))

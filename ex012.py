# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE E OFEREÇA 5% DE DESCONTO

p = float(input('Digite o valor do produto em reais: R$'))

print('O produto custa R${:.2f}, com desconto de 5% ele custa R${:.2f}' .format(p, p * 0.95))


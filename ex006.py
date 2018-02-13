# LEIA UM NÚMERO E MOSTRE SEU DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input('Digite um número: '))

print('Número digitado: {} \n Seu dobro: {} \n Seu triplo: {} \n ' .format(n, (n*2), (n*3)))
print('Sua raiz quadrada: {:.2f}' .format((n**(1/2))))

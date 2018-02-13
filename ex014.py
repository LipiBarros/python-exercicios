# FAÇA UM PROGRAMA QUE LEIA UMA TEMPERATURA EM ºC E CONVERTA PARA ºF

celsius = float(input('Digite uma temperatura em ºC: '))

farenheit = (celsius * 9/5) + 32

print('A temperatura de {:.2f}ºC, equivale a {:.2f}ºF '.format(celsius, farenheit))

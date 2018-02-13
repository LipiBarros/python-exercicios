import math

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

real = float(input('Digite um número real:'))

print('A parte inteira do número {} é {}'.format(real, math.trunc(real)))

# ALTERNATIVA AO USO DE BIBLIOTECA MATH
# print('A parte inteira do número {} é {}'.format(real, int(real)))

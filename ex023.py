'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS
EX: DIGITE UM NÚMERO: 1834
- UNIDADE: 4
- DEZENA: 3
- CENTENA: 8
- MILHAR: 1

OBS: TENTAR FAZER USANDO STRINGS E MÓDULO MATEMÁTICOS'''

#USANDO MÓDULOS MATEMÁTICOS

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade = {}'  .format(u))
print('Dezena = {}'  .format(d))
print('Centena = {}'  .format(c))
print('Milhar = {}'  .format(m))



#USANDO STRINGS E ESTRUTURAS DE REPETIÇÃO
'''num = input('Digite um número entre 0 e 9999: ')

size = len(num)

if size == 4:
    milhar = num[0]
    centena = num[1]
    dezena = num[2]
    unidae = num[3]
if size == 3:
    milhar = ''
    centena = num[0]
    dezena = num[1]
    unidae = num[2]
if size == 2:
    milhar = ''
    centena = ''
    dezena = num[0]
    unidae = num[1]
if size == 1:
    milhar = ''
    centena = ''
    dezena = ''
    unidae = num[0]

print('Unidade = {}' .format(unidae))
print('Dezena = {}' .format(dezena))
print('Centena = {}' .format(centena))
print('Milhar = {}' .format(milhar))'''

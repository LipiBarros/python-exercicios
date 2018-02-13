# DIGITE ALGO NA TELA E MOSTRE TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE O QUE FOI DIGITADO

n = input('Digite algo: ')

print('Tipo primitivo é {}'.format(type(n)))
print('Só tem espaços ? {}' .format(n.isspace()))
print('É um número ? {}' .format(n.isnumeric()))
print('É alfabético ? {}' .format(n.isalpha()))
print('É alfanumérico ? {}' .format(n.isalnum()))
print('Está em maiúsculas ? {}' .format(n.isupper()))
print('Está em minúsculas ? {}' .format(n.islower()))
print('Está captalizada ? {}' .format(n.istitle()))

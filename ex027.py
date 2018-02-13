'''FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE

EX: Ana Maria de Souza
primeiro = Ana
último = Souza

OBS: DEVE FUNCIONAR PARA QUALQUER TAMANHO DE STRING'''

nome = str(input('Digite seu nome completo: ')).strip()

lista = nome.split()

print('Primeiro nome: {}' .format(lista[0]))
print('Último nome: {}' .format(lista[len(lista) - 1]))

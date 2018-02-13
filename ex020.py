# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS.
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)


'''al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro aluno: ')
al4 = input('Nome do quarto aluno: ')

s = set(range(1, 5))
seq = 1

while len(s) > 0:
    sort = random.choice(list(s))
    s.remove(sort)

    if sort == 1:
        aluno = al1
    if sort == 2:
        aluno = al2
    if sort == 3:
        aluno = al3
    if sort == 4:
        aluno = al4
    # print('Numero sorteado:{}'.format(sort))
    print('Aluno {}: {}'.format(seq, aluno))
    seq = seq + 1'''


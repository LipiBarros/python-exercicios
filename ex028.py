#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NÚMERO INTEIRO ENTRE 0 E 5
#E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
#O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

from random import randint
from time import sleep

num = randint(0, 5)
print('-=-' * 30)
print('Estou pensando em um número entre 0 e 5, será que você consegue advinhar ?')
print('-=-' * 30)
op = int(input('Digite seu palpite: '))
print('PROCESSANDO...')
sleep(2)
if op == num:
    print('YOU WIN!!!')
else:
    print('GAME OVER!!!')
print('Minha escolha foi o número {} !' .format(num))

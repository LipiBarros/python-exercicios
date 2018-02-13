# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO
# PARA SALÁRIOS SUPERIORES A R$1250,00 CALCULE UM AUMENTO DE 10%
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

sal = float(input('Qual o salário do funcionário ? R$ '))

if sal > 1250.00:
    nsal = sal * 1.10
else:
    nsal = sal * 1.15
print('Quem ganhava R${:.2f} reais, passa a ganhar R${:.2f}' .format(sal, nsal))

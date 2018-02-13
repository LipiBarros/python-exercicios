'''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
- O NOME COM TODAS AS LETRAS MAIÚSCULAS
- O NOME COM TODAS AS LETRAS MINÚSCULAS
- QUANTAS LETRAS AO TODO (SEM CONTAR OS ESPAÇOS)
- QUANTAS LETRAS TEM O PRIMEIRO NOME'''


nome = str(input('Digite seu nome completo: ')).strip()
#nome_ = ''.join(nome.split())

print('Nome em maiúsculas: {}'.format(nome.upper()))
print('Nome em minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))
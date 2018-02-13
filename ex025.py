# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

nome = str(input('Digite um nome: ')).strip()

print('O nome contém "Silva" ? {}'.format('SILVA' in nome.upper()))

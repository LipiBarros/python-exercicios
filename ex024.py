'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO" '''

cidade = str(input('Digite o nome de uma cidade: ')).strip()

resultado = 'SANTO' in cidade.upper()[:5]

print('A cidade {} começa com o nome "SANTO" ? {}' .format(cidade, resultado))

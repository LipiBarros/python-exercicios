# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO
# SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO

print('Digite 3 segmentos de reta, para verificarmos se é possível existir um triângulo.')
a = float(input('Digite o valor do segmento A: '))
b = float(input('Digite o valor do segmento B: '))
c = float(input('Digite o valor do segmento C: '))

if a < b + c and b < a + c and c < a + b:
            print('Com os segmentos {}, {} e {} podemos formar um triângulo.' .format(a, b, c))
else:
    print('Com os segmentos {}, {} e {} NÃO podemos formar um triângulo.'.format(a, b, c))

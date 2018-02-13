# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

from calendar import isleap
from datetime import date
ano = int(input('Digite um ano para verificarmos se é bissexto, digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print('O ano de {} é bissexto!' .format(ano))
else:
    print('O ano de {} não é bissexto.' .format(ano))

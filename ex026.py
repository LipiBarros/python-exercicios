'''FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
- QUANTAS VEZES APARECE A LETRA "A"
- EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
- EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ'''

frase = str(input('Digite uma frase qualquer: ')).strip()

qt_a = frase.upper().count('A')
first_a = frase.upper().find('A')
last_a = str.rfind(frase.upper(), 'A')

print('A frase, "{}", possui:' .format(frase))
print('Quantidades de letra "A" ? {}'.format(qt_a))
print('Posição da primeira letra "A" ? {}' .format(first_a + 1))
print('Posição da última letra "A" ? {}' .format(last_a + 1))

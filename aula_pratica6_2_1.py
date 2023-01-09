# Escreva um algoritmo que crie uma tupla com 5 palavras.
# Encontre dentro dessa tupla as vogais de cada palavra.
# Faça um print na tela com o nome da palavra e suas respectivas vogais

palavras = ('Mario', 'Luigi', 'Peach','Yoshi','Bowser')

for palavra in palavras:
    print('\n Palavra:{}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(),end=' ')
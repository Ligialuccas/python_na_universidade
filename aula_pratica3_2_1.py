# Faça um algoritmo que receba três valores,
# Representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como
# a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)

a = int(input('Digite o 1º lado do triângulo: '))
b = int(input('Digite o 1º lado do triângulo: '))
c = int(input('Digite o 1º lado do triângulo: '))

if (a > 0) and (b > 0) and (c > 0):
    if (a + b > c) and (a + c > b) and (b + c > a):
   #se você chegou até aqui, é porque o triângulo é válido!
        if (a != b) and (a != c) and (b != c) :
            print('Triangulo escaleno!')
        else:
            if (a == b) and (a == c):
                print('Triângulo equilátero!')
            else:
                print('Triângulo isóceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')

else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')
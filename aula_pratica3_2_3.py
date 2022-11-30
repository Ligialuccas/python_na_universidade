#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o tipo de instalação
# R para Residências, I para Industrias e C para Comércios


kwh = float(input('Quantos kWh?'))
tipo = input('Qual o tipo de instalação (R, C, I)')


if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif (tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif (tipo == 'I' ):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print ('Instalação invalida!')

print ('Total a pagar: {}'.format(kwh * preco))
#Exercicio 2
#Escreva um progama que pergunte a quantidade de km percorridos por um carro alugado pelo usuario
#Assim como a quantidade de dias pelos quais o carro foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0,15 por km rodado

kilometros = int(input('Quantos Kilometros foram percorridos: '))
dias = float(input('Por quantos dias o carro foi alugado: '))

total_dias = dias * 60
total_km = kilometros * 0.15
valor_total = total_km + total_dias
print('Kilometros = {}. Dias = {}'.format(kilometros,dias))
print('O valor total a ser pago pelo aluguel do carro é de: R$ {}'.format(valor_total))
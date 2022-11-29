#Exercicio 1
#Desenvolva um algoritmo que solicite ao usuario o preço de um produto e um percentual de desconto a ser aplicado a ele.
#calcule e exiba o valor do desconto e o preço final do produto

preco = float(input('Digite o preço do Produto: ' ))
p = float(input('Digite o percentual de desconto(0-100)%: ' ))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}%'.format(preco,p))
print('O valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto,final))






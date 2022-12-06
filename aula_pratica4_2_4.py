"""
Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa.
Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito,
Se tiver entre 3 e 12 anos, o ingresso custará R$15,
Se tiver mais de 12 anos, custará R$30.
"""
#Escreva um laço, em que você pergunte a idade aos usuários e, então, informe-lhes o preço do ingresso do cinema
#Encerre o laço udsando um break quando o usuário digitar sair
#Após encerrar o laço, apresente na tela o total de pessoass que compraram ingressos, o total de dinheiro arrecadado
#E a média de idade das pessoas


total = 0
dinheiro = 0
while True:
    idade = input('Qual sua idade? ')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: {}'.format(dinheiro))
print('Média arrecadada: {}'.format(media))


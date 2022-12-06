print('Bem-vindo a empresa da Ligia Almeida Luccas')

#variáveis
valor_produto = float(input('Entre com o valor unitário do produto: '))
qtd_produto = int(input('Entre com a quantidade desse produto: '))
custo_embalagem = 0

# uso do if, elif, else
if qtd_produto < 11:
  custo_embalagem = 30.00
elif 11 <= qtd_produto <101:
  custo_embalagem = 60.00
elif 101 <= qtd_produto <1001:
  custo_embalagem = 120.00
else:
  custo_embalagem = 240.00

#variáveis
total_sem_embalagem = valor_produto * qtd_produto
print('O valor total sem o custo da embalagem para frete é de {:.2f}'.format(total_sem_embalagem))
total_com_embalagem = total_sem_embalagem + custo_embalagem
print('O valor total com o custo da embalagem para frete é de {:.2f}'.format(total_com_embalagem))
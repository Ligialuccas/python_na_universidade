#Crie uma variavel de string que receba uma frase qualquer.
#Crie uma segunda variavel, agora contedo a metade da string digitada.
#Imprima na tela somente os dois ultimos caracteres da segunda variavel do tipo string

frase = input('Digite uma frase: ')
tamanho = len(frase)

frase2 = frase[:int(tamanho/2)]

print(frase2[-2:])


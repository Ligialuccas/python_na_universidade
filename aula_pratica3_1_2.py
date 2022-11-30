# 1) Traduza as afirmações a seguir para condicionais

# a) Se a idade é maior que 60, escreva: "Você tem direito aos benefícios".

idade = 75
if idade >= 60:
    print('Você tem direito aos benefícios')

# b) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você está morto!".

dano = 15
escudo = 0
if dano > 10 and escudo == 0:
    print('Você está morto!')

# c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!".

norte = False
sul = False
leste = True
oeste = False
if (norte == True or sul == True or leste == True or oeste == True):
    print('Você escapou!')

#outra opção

if (norte or sul or leste or oeste):
    print('Você escapou!')




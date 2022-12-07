#Suponha que você é um colecionador de jogos de videogame.
#Escreva um algoritmo que permita cadastrar esses jogos informando o nome e a qual videogame ele pertence
#Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado e sair
#Para resolver esse exercício, crie pelo menos uma função para cada item do menu
#Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados


def valida_int(pergunta, min, max):
    """
    Função para validar dados
    :param pergunta:
    :param min:
    :param max:
    :return:
    """
    x = int(input(pergunta))
    while ((x <min) or (x > max)):
        x = int(input(pergunta))
    return x

def borda(s1):
  tam = len(s1)
  #só imprime caso exista algum caractere
  if tam:
    print('+','-' * tam, '+')
    print ('|', s1, '|')
    print('+','-' * tam, '+')

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo,'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideogame))
    finally:
        a.close()


#Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    borda('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op ==1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break







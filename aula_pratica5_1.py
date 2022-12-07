#Criando help para função

def soma(x = 0, y = 0, z = 0):
    """
    Função que soma até 3 valores inteiros
    :param x: valor inteiro opcional
    :param y: valor inteiro opcional
    :param z: valor inteiro opcional
    :return: soma inteira
    """
    return x + y + z


print (soma(3,2))
help(soma)
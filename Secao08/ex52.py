'''
51. Escreva uma funcao que recebe uma matriz quadrada de ordem N e calcule a sua trans- 
posta (se B e a matriz transposta de A entao aij = bji).
'''


def matriz_transposta(matriz):
    """
    Função que recebe uma matriz quadrada de ordem N e retorna a sua transposta
    :param matriz: Recebe uma matriz quadrada de ordem N
    :return: Retorna a matriz transposta da matriz recebida por parâmetro.
    Caso não seja uma matriz quadrada, retorna um valor do tipo None
    """

    transposta = []

    quadrada = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not(len(matriz) == len(matriz[i])):
                quadrada = False

    if quadrada:
        for i in range(len(matriz)):
            matriz = []

            for j in range(len(matriz[i])):
                matriz.append(matriz[j][i])

            transposta.append(matriz)

        return transposta



if __name__ == '__main__':

    matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()







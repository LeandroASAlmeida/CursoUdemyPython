'''
58. Faca uma funcao que receba, por parametro, duas matrizes quadradas de orden N, A e 
B, e retorna uma matriz C, tambem por parametro, que seja o produto matricial de A e B
'''


def nova_matriz(n_a, n_b):
    quad_a = True
    quad_b = True

    for l in range(len(n_a)):
        for c in range(len(n_a[l])):
            if not (len(n_a) == len(n_a[l])):
                quad_a = False

    for l in range(len(n_b)):
        for c in range(len(n_b[l])):
            if not (len(n_b) == len(n_b[l])):
                quad_b = False

    if quad_a and quad_b:
        matriz_c = []

        if len(n_a) >= len(n_b):
            for l in range(len(n_a)):
                matriz = []
                for c in range(len(n_a[l])):
                    matriz.append(n_a[l][c])

                matriz_c.append(matriz)

            for l in range(len(n_b)):
                for c in range(len(n_b[l])):
                    matriz_c[l].append(n_b[l][c])

        else:
            for l in range(len(n_b)):
                matriz = []
                for c in range(len(n_b[l])):
                    matriz.append(n_b[l][c])

                matriz_c.append(matriz)

            for l in range(len(n_a)):
                for c in range(len(n_a[l])):
                    matriz_c[l].append(n_a[l][c])

        return matriz_c


if __name__ == '__main__':

    matriz_1 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]
    matriz_2 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]

    for l in range(0,4):
        for c in range (0,4):
            matriz_1[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
    print('-=' * 30) # linha de separação
    for l in range(0,4):
        for c in range(0,4):
            print(f'[{matriz_1[l][c]:^5}]', end ='')
        print()
    print('-=' * 30) # linha de separação
    for l in range(0,4):
        for c in range (0,4):
            matriz_2[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
    print('-=' * 30) # linha de separação
    for l in range(0,4):
        for c in range(0,4):
            print(f'[{matriz_2[l][c]:^5}]', end ='')
        print()
print(f"Nova matriz:")
print('-=' * 30) # linha de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'{nova_matriz(matriz_1, matriz_2)}', end ='')
        print()

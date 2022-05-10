'''
54. Faca uma funcao que recebe, por parametro, uma matriz A[3][3] e retorna a soma dos 
elementos da sua diagonal principal e da sua diagonal secundaria 

'''
def diagonal_principal(a):
    tamanho = True
    soma_p = 0

    if len(a) == 3:
        for i in range(len(a)):
            if len(a[i]) == 3:
                for j in range(len(a[i])):
                    soma_p = a[0][0] + a[1][1] + a[2][2]
            else:
                tamanho = False

        if tamanho:
            return soma_p

def diagonal_secundaria(b):
    tamanho = True
    soma_s = 0
 

    if len(b) == 3:
        for i in range(len(b)):
            if len(b[i]) == 3:
                for j in range(len(b[i])):
                    soma_s = b[0][2] + b[1][1] + b[2][0]
            else:
                tamanho = False

        if tamanho:
            return soma_s

if __name__ == '__main__':

    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for l in range(0,3):
        for c in range (0,3):
            matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
    print('-=' * 30) # linha de separação
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]', end ='')
        print()
    print('-=' * 30) # linha de separação
    print(f"Soma da sua diagonal principal: {diagonal_principal(matriz)}")
    print(f"Soma da sua diagonal secundária: {diagonal_secundaria(matriz)}")
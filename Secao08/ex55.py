'''
54. Faca uma funcao que recebe, por parametro, uma matriz A[3][3] e retorna a soma dos 
elementos da sua diagonal principal e da sua diagonal secundaria 

'''
def diagonal_principal(a):
    tamanho = True
    soma_p = 0
    soma_s = 0

    if len(a) == 4:
        for i in range(len(a)):
            if len(a[i]) == 4:
                for j in range(len(a[i])):
                    soma_p = a[0][0] + a[1][1] + a[2][2]
            else:
                tamanho = False

        if tamanho:
            return soma_p

def diagonal_secundaria(a):

      tamanho = True
 

    if len(a) == 4:
        for i in range(len(a)):
            if len(a[i]) == 4:
                for j in range(len(a[i])):
                    soma_s = a[0][0] + a[1][1] + a[2][2]
            else:
                tamanho = False

        if tamanho:
            return soma_s

    if __name__ == '__main__':

        matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for l in range(0,4):
        for c in range (0,4):
            matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
    print('-=' * 30) # linha de separação
    for l in range(0,4):
        for c in range(0,4):
            print(f'[{matriz[l][c]:^5}]', end ='')
        print()
    print('-=' * 30) # linha de separação
    print(f"Soma da sua diagonal principal: {diagonal_principal(matriz)}")
    print(f"Soma da sua diagonal secundária: {diagonal_secundaria(matriz)}")
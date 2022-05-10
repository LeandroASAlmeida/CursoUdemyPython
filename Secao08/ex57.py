'''
56. Faca uma funcao que recebe, por parametro, uma matriz A[7][6] e uma coluna N e retorne 
a soma dos elementos dessa coluna.

'''

def soma_n(n, a):

    soma = 0
    tamanho = True

    if len(a) == 7:
        for l in range(len(a)):
            if len(a[l]) == 6:
                for c in range(len(a[l])):
                    if c == n:
                        soma += a[l][c]

            else:
                tamanho = False

        if tamanho:
            return soma


if __name__ == '__main__':

    matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
    n = 0

    for l in range(0,7):
        for c in range (0,6):
            matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
    print('-=' * 30) # linha de separação
    for l in range(0,7):
        for c in range(0,6):
            print(f'[{matriz[l][c]:^5}]', end ='')
        print()
    print('-=' * 30) # linha de separação
    n=int(input('Qual a coluna que deseja saber a soma (0 á 6): '))
print(f"Soma dos elementos da coluna n {n}: {soma_n(n, matriz)}")


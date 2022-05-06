'''
53. Faca uma funcao que recebe, por parametro, uma matriz A[4][4] e retorna a soma dos 
seus elementos.

'''
def soma_elementos(a):
    tamanho = True
    soma = 0

    if len(a) == 4:
        for i in range(len(a)):
            if len(a[i]) == 4:
                for j in range(len(a[i])):
                    soma += a[i][j]
            else:
                tamanho = False

        if tamanho:
            return soma

if __name__ == '__main__':

    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0,4):
    for c in range (0,4):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
print('-=' * 30) # linha de separação
print(f"Soma dos elementos da matriz: {soma_elementos(matriz)}")
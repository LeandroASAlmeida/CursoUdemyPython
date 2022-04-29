'''3. Faca um programa que preenche uma matriz com o produto do valor da linha e da coluna
de cada elemento. Em seguida, imprima na tela a matriz.'''


matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for l in range(0,5):
    for c in range(0,5):
        matriz[l][c] = l * c

for l in range(0,5):
    for c in range(0,5):
        print(matriz[l][c], end=' ')
    print( )
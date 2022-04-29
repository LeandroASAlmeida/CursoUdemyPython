'''6. Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posicao
das matrizes lidas.'''

matriz_1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz_2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matriz_3=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

maior_valor = int()
maior_l = 0
maior_c = 0

for l in range(0,4):
    for c in range (0,4):
        matriz_1[l][c] = int(input(f'Digite um valor para a Matriz 0 [{l},{c}]: '))
        matriz_2[l][c] = int(input(f'Digite um valor para a Matriz 1 [{l},{c}]: '))

for l in range(0,4):
    for c in range(0,4):
        if matriz_1[l][c] >= matriz_2[l][c]:
           matriz_3[l][c] = matriz_1[l][c]
        elif matriz_1[l][c] < matriz_2[l][c]:
            matriz_3[l][c] = matriz_2[l][c]


print("Matriz 0: ")
print('-=' * 30) # l de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_1[l][c]:^5}]', end ='')
    print( )

print("Matriz 1: ")
print('-=' * 30) # l de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_2[l][c]:^5}]', end ='')
    print( )

print("Matriz 2: ")
print('-=' * 30) # l de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_3[l][c]:^5}]', end ='')
    print( )



'''7. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos sao da forma: 
A[i][j] = 2*i + 7*j 2 se i < j;
A[i][j] = 3*i^2 1 se i = j ;
A[i][j] = 4*i^3 5*j^2 + 1 se i > j.'''


matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for l in range(10):
    for c in range(10):
        matriz[l][c] = int(input(f'Digite um valor para a Matriz 0 [{l},{c}]: '))
        if l < c:
            matriz[l].append((2*l)+(7*c))
        elif l == c:
            matriz[l].append((3*(l**2))-1)
        else:
            matriz[l].append((4*(l**3))-(5*(c**2)+1))

for i in range(0,10):
    for c in range(0,10):
        print(f"[{matriz[l][c]:^5}]", end=' ') #  ^5} tamanho do espaço da impressão da matriz
    print( )



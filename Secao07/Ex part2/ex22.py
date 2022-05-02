'''22. Faca um programa que leia duas matrizes A e B de tamanho 3 x 3 e calcule C = A ∗ B.'''

aa = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
be = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
ce = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):
        aa[l][c] = int(input(f"Defina um valor para a posição [{l}][{c}] da matriz A: "))
        be[l][c] = int(input(f"Defina um valor para a posição [{l}][{c}] da matriz B: "))
        ce[l][c] = aa[l][c] * be[l][c]

print("Matriz A:")

for l in range(0,3):
    for c in range(0,3):
        print(f"[{aa[l][c]:^5}]", end='')
    print( )

print("Matriz B:")

for l in range(0,3):
    for c in range(0,3):
        print(f"[{be[l][c]:^5}]", end='')
    print( )

print("Matriz Ce:")

for l in range(0,3):
    for c in range(0,3):
        print(f"[{ce[l][c]:^5}]", end='')
    print( )
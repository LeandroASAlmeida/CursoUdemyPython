'''23. Faca um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A2
'''

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):
        a[l][c] = int(input(f"Informe um valor para a posição [{l}][{c}] da matriz A: "))
        b[l][c] = a[l][c] ** 2  # 5 elevado ao quadrado

print("Matriz A:")

for l in range(0,3):
    for c in range(0,3):
        print(f"[{a[l][c]:^5}]", end='')
    print()

print("Matriz B:")

for l in range(0,3):
    for c in range(0,3):
        print(f"[{b[l][c]:^5}]", end='')
    print()
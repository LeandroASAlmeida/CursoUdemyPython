'''12. Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
transposta = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        transposta[c][l] = matriz[c][l]
        print(f'[{transposta[c][l]:^5}]', end ='')
    print()
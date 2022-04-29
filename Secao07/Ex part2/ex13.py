'''13. Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme
a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada''' 


matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
m_triângular=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for l in range(0,4):
    for c in range (0,4):
        matriz[l][c] = int(input(f'Digite valores no intervalo de [1, 20] para a posição [{l}][{c}]: '))
        while matriz[l][c] < 1 or matriz[l][c] > 20:
              matriz[l][c] = int(input(f'Valor Inválido.Use somente valores no intervalo  de [1, 20] para a posição [{l}][{c}]: '))

print('-=' * 30) # linha de separação

print("Matriz Original: ")
for l in range(0,4):
        for c in range(0,4):
            print(f"[{matriz[l][c]:^5}]", end=' ')
        print( )
for l in range(0,4):
        for c in range(0,4):
            if l == 0 and c >= 1:
                matriz[l][c] = 0
            elif l == 1 and c >= 2:
                matriz[l][c] = 0
            elif l == 2 and c == 3:
                matriz[l][c] = 0

print("Matriz trinângular: ")
for l in range(0,4):
    for c in range(0,4):
        print(f"[{matriz[l][c]:^5}]", end=' ')
    print( )












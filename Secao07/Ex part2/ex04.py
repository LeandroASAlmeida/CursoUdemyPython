'''4. Leia uma matriz 4 x 4, imprima a matriz e retorne a localizacao (linha e a coluna) do 
maior valor.'''

matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
maior_valor = int()
maior_linha = 0
maior_coluna = 0

for l in range(0,4):
    for c in range (0,4):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz[l][c]:^5}]', end ='')
        for l in range(0,4):
            for c in range(0,4):
                if matriz[l][c] > maior_valor:
                    maior_valor = matriz[l][c]
                    maior_linha = l
                    maior_coluna = c
    print()

print(f"O maior valor da matriz é {maior_valor}, que está na linha {maior_linha} e na coluna {maior_coluna}.")



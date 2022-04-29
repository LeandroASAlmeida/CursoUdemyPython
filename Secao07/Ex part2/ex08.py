'''8. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao acima da 
diagonal principal.'''


matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=0

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
        if l <= c:
            soma += matriz[l][c]
    print()    
           
print(f"A soma entre os valores acima da diagonal principal é {soma}.")

'''11. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao na diago- 
nal secundaria.'''

matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=0

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
        if c == l:
            soma += matriz[l][c]
    print()    
           
print(f"A soma entre os valores que estão na diagonal segundaria é {soma}.")
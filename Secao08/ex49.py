'''
48. Faca uma funcao que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma 
dos elementos que estao abaixo da diagonal principal. 
'''

def abaixo_diagonal(v):
    soma= 0
   
    soma= v[1][0]+v[2][0]+v[2][1]
    return soma


if __name__ == '__main__':

    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
print(f"Soma dos elementos que estão acima da diagonal principal: {abaixo_diagonal(matriz)}")

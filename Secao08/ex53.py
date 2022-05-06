'''
52. Faca uma funcao que verifica se uma matriz quadrada de ordem N e a matriz identidade.
'''

def identidade(n):
 
                    
if __name__ == '__main__':

    matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        
print('-=' * 30) # linha de separação

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
for i in range(3):
    print(matriz[i])

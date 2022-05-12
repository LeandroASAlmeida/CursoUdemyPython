'''
51. Escreva uma funcao que recebe uma matriz quadrada de ordem N e calcule a sua trans- 
posta (se B e a matriz transposta de A entao aij = bji).
'''

def m_transposta(n):
    transposta = []

    for l in range(0,3):
        for c in range(0,3):
           
        return transposta
            

if __name__ == '__main__':

    matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
print('-=' * 30) # linha de separação
print(f"Matriz transposta {m_transposta(matriz)}")




'''
46. Faca uma funcao que receba uma matriz 4 x 4 e retorne quantos valores maiores do que 
10 ela possui.
'''

def maior_dez(v):

    tam = True
    quant = 0

    if len(v) == 4:
        for i in range(len(v)):
            if len(v[i]) == 4:
                for j in range(len(v[i])):
                    if v[i][j] > 10:
                        quant += 1
            else:
                tam = False  
        if tam:
            return quant

if __name__ == '__main__':

    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for l in range(0,4):
    for c in range (0,4):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()

print(f"Quantidade de valores maiores que 10: {maior_dez(matriz)}")
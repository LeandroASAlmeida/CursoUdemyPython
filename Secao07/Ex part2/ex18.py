'''18. Faca um programa que permita ao usuario entrar com uma matriz de 3 x 3 numeros 
inteiros. Em seguida, gere um array unidimensional pela soma dos numeros de cada 
coluna da matriz e mostrar na tela esse array. Por exemplo, a matriz:
5 -8 10
1 2 15
25 10 7
Vai gerar um vetor, onde cada posicao e a soma das colunas da matriz. A primeira 
posicao ser a 5 + 1 + 25, e assim por diante: 
31 4 3'''


matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=0
vetor=[]

for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30) # linha de separação

for l in range(0,3):
    soma += matriz[l][0]
vetor.append(soma)
soma = 0

for l in range(0,3):
    soma += matriz[l][1]
vetor.append(soma)
soma = 0

for l in range(0,3):
    soma += matriz[l][2]
vetor.append(soma)

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=' ')
    print( )
print(vetor)
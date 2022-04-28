'''
3. Faca um programa que leia um vetor de 15 posioes e o compacte, ou seja, elimine as 
posicoes com valor zero. Para isso, todos os elementos a frente do valor zero, devem ser `
movidos uma posicao para tras no vetor

'''

vetor=[]

print('VETOR 1:')
for i in range(0,15):
    vetor.append(int(input(f'Digite o {i+1}º número de Vetor: ')))

for i in range(14, -1, -1):
    if vetor[i] == 0:
        vetor.pop(i)

print(vetor)
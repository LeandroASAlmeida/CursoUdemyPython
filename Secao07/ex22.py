'''
22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor
contendo, nas posições pares os valores do primeiro e nas posições impares os valores
do segundo

'''

vetor1=[]
vetor2=[]
outro_vetor= []

print('Preencha o vetor 1:')
for i in range(0,10):
    vetor1.append(int(input(f'V1[{i}]: '))) # [{i}]colocar o indice
print('Preencha o vetor 2:')
for i in range(0,10):
    vetor2.append(int(input(f'V2[{i}]: ')))

print('O Outro vetor irá receber os seguintrs valores: ')
for i in range(len(vetor1)):
    outro_vetor.append(vetor1[i])
    outro_vetor.append(vetor2[i])

print(outro_vetor)




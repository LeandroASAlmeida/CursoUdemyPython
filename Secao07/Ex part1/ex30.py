'''30. Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
interseccao entre os 2 vetores anteriores, ou seja, que contem apenas os numeros que 
estao em ambos os vetores. Nao deve conter numeros repetidos.'''

vetor1=[]
vetor2=[]
vetor_inter= []

print('VETOR 1:')
for i in range(0,10):
    vetor1.append(int(input(f'Digite o {i+1}º número de V1: ')))

print('VETOR 2:')
for i in range(0,10):
    vetor2.append(int(input(f'Digite o {i+1}º número de V2: ')))

vetor1 = set(vetor1)
vetor2 = set(vetor2)
vetor_inter = vetor1.intersection(vetor2) # O intersection retorna um conjunto que contém a semelhança entre dois ou mais conjuntos.

print(f'\nIntersecção entre v1 e v2: \n{vetor_inter}')
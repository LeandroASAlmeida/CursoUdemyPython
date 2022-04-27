'''
31. Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a uniao
entre os 2 vetores anteriores, ou seja, que contem os numeros dos dois vetores. Nao
deve conter numeros repetidos. 

'''

vetor1=[]
vetor2=[]
vetor_union= []

print('VETOR 1:')
for i in range(0,10):
    vetor1.append(int(input(f'Digite o {i+1}º número de V1: ')))
print(vetor1)

print('VETOR 2:')
for i in range(0,10):
    vetor2.append(int(input(f'Digite o {i+1}º número de V2: ')))
print(vetor2)

vetor1 = set(vetor1)
vetor2 = set(vetor2)
vetor_union = vetor1.union(vetor2)

print(vetor_union)

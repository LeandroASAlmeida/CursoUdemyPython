'''
36. Leia um vetor com 10 numeros reais, ordene os elementos deste vetor, e no final escreva 
os elementos do vetor ordenado.
'''

vetor=[]


print('VETOR 1:')
for i in range(0,10):
    vetor.append(float(input(f'Digite o {i+1}º número real: ')))


vetor.sort()
print(vetor)


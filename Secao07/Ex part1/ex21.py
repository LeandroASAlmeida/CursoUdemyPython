'''
21. Faça um programa que receba do utilizador dois vetores, A e B, com 10 números
inteiros cada. Crie um novo vetor denominado C calculando C = A - B. Mostre no ecrã
os dados do vetor C.

'''
a=[]
b=[]
c=[]

print('Preencha o vetor A:')
for i in range(10):
    a.append(int(input(f'A[{i}]: '))) # [{i}]colocar o indice
print('Preencha o vetor B:')
for i in range(10):
    b.append(int(input(f'B[{i}]: ')))


    c.append(a[i] - b[i])

print(f'Vetor C = A - B \n{c}')


 
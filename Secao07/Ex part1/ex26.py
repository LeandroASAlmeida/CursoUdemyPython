'''
Faca um programa que calcule o desvio padrao de um vetor v contendo n = 10 numeros,
onde m e a media do vetor.  Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)

'''
v = []

print('Preencha o vetor V:')
for i in range(0,10):
    v.append(int(input(f'V[{i}]: '))) # [{i}]colocar o indice

n = len(v) # tamanho da lista
m = sum(v) / n # soma da lista

quadrado = 0
for i in v:
    quadrado += (i - m) ** 2

desvio = (quadrado / n) ** 0.5

print(f"\nO desvio Padrão é : {desvio}")
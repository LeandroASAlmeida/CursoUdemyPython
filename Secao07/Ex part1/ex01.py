'''
1. Faça um programa que possua um vetor denominado A que armazene 6 números
inteiros. O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma varável inteira (simples) a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre no ecrã esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre no ecrã cada valor do vetor A, um em cada linha.

'''


a = [1,0,5,-2,-5,7]
print (a)

soma = a[0] + a[1] + a[5]
print(soma)

a.insert(4,'100')
print(a)

for valor in a:
   print(valor)
'''
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n
linhas do chamado Triangulo de Pascal:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

'''

n = [1]
num= 0

num = int(input(f"Digite um valor para  gerar o triaâgulo de pacoal: "))

for i in range (num):
    print(n)
    n.append(0)
    w=[1]
    for j in range(len(n)):
        if j > 0:
           w.append(n[j-1]+n[j]) 
    n=w


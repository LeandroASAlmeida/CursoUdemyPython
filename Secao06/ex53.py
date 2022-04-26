'''Escreva um programa que leia um numero inteiro positivo  n e em seguida imprima n
linhas do chamado Triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
'''

num_linhas= int(input('Informe um numero inteiro e positivo para gerar o triângulo de Floyd: '))
colunas = 1

for c in range(1, num_linhas + 1):
    for i in range(1, c + 1):
        print(f'{colunas:<4}', end='')
        colunas += 1
    print()
    


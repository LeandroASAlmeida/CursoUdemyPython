'''Faca um programa que leia um numero inteiro positivo ımpar N e imprima todos os
numeros ımpares de 1 ate N em ordem decrescente'''

n = int(input('Digite um número inteiro,positivo,par e diferente de 0: '))

while n <= 0:
        print('Número inválido.')
        n = int(input('Digite um número inteiro,positivo,par e diferente de 0: '))
while n % 2 == 0:
        print('Número inválido.')
        n = int(input('Digite um número inteiro,positivo,par e diferente de 0: '))

if n > 1:
    if n % 2 != 0:
        for x in range(n,-1,-1):# descrescente
            if x % 2 != 0:
                print(x)

   
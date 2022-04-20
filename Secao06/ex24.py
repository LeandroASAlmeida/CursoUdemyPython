'''
Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores 
desse numero, com excecao dele proprio. Ex: a soma dos divisores do numero 66  e
1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
'''
divisor = 1
soma = 0

while True:
    numero = int(input('Digite um número inteiro: '))

    for divisor in range(divisor, numero):
        if numero % divisor == 0:
            soma += divisor
    print(soma)